# @allure.id("ITCH-1")
# @allure.story("стори")
# @allure.feature("фича")
# @allure.epic("эпик")
# @allure.title("заголовок")
# @allure.description("описание")
# @allure.severity("minor") # blocker / critical / normal / minor / trivial

# @pytest.mark.skip(reason="Skipping for demo")

# def test_one():
#     with allure.step("step one"):
#         # тело функции

# Run commands
# - TO generate the report:
# pytest --alluredir=allure-results
# - TO run the generated report:
# allure serve allure-results
# Optional flag (for MacOS): --host 127.0.0.1
# - TO generate the local report:
# allure generate allure-results -o allure-report
# Optional flag (to rewrite the existing local report): --clean
# - TO run the generated local report:
# allure open allure-report
# Optional flag (for MacOS): --host 127.0.0.1

# Setup Guide:
# — To install Allure:
# pip install pytest allure-pytest
# — To check if Allure is installed:
# pip show allure-pytest
# — IF on Windows Allure is not recognized, then:
# scoop install allure (In Powershell)
# — IF on Windows scoop is not recognized, then:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
# — IF on Windows JAVA is not recognized, then:
# java --version
# — IF on Windows JAVA is not installed, then:
# https://www.oracle.com/java/technologies/downloads/ > JDK 25 > Windows > x64 Installed download > Install
# — IF on Windows JAVA is still not recognized, then:
# Restart terminals