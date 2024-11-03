import subprocess

def install_packages_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # 파일의 모든 줄 읽기
        lines = file.readlines()

    packages = [line.strip() for line in lines if line.strip()]  # 공백 제거

    if packages:
        # pip 명령어 실행
        command = ["pip", "install"] + packages
        print("Installing packages:", ", ".join(packages))
        try:
            subprocess.run(command, check=True)
            print("Installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during installation: {e}")
    else:
        print("No packages found to install.")

# 사용 예: 패키지 목록이 저장된 텍스트 파일의 경로를 지정
install_packages_from_file('/home/bongjae/바탕화면/test/requirements.txt')
