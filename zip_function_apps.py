import shutil

V2_LANGUAGES = {
    'python': ['36', '37'],
    'node': ['8', '10'],
    'dotnet': ['2']
}

RUNTIMES_TEST_MATRIX = {
    'v2': V2_LANGUAGES
}

if __name__ == '__main__':
    for runtime, languages in RUNTIMES_TEST_MATRIX.items():
        for language, versions in languages.items():
            for version in versions:
                zip_name = f'{runtime}_{language}_{version}'
                zip_path = f'azure-functions-devops-cli-test/test_apps/{runtime}/{language}/{version}'
                shutil.make_archive(zip_name, 'zip', zip_path)
