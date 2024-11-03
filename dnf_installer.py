import subprocess

def install_packages_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # 파일의 모든 줄 읽기
        lines = file.readlines()

    packages = []
    for line in lines:
        # 패키지 이름과 버전 추출
        parts = line.split()
        if len(parts) >= 2:
            package_name_with_arch = parts[0]
            package_version = parts[1]
            package_name = package_name_with_arch.split('.')[0]  # 아키텍처 부분 제거
            packages.append(f"{package_name}-{package_version}")

    if packages:
        # dnf 명령어 실행
        command = ["sudo", "dnf", "install"] + packages
        print("Installing packages:", ", ".join(packages))
        try:
            subprocess.run(command, check=True)
            print("Installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during installation: {e}")
    else:
        print("No packages found to install.")

# 사용 예: 패키지 목록이 저장된 텍스트 파일의 경로를 지정
install_packages_from_file('/home/bongjae/바탕화면/test/dnf_installed_packages.txt')
