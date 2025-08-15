import sys
import platform
from config import settings



def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    items.append(f'system={platform.system()},{platform.release()}')
    items.append(f'py_version={sys.version}')
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл