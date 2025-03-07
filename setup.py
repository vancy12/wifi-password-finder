import setuptools

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()

setuptools.setup(
    name="wifi-password",
    version="1.1.1",
    author="Saanvi Shet",
    author_email="saanvishet12@gmail.com",
    description="Quickly fetch your WiFi password and if needed, generate a QR code of your WiFi to allow phones to easily connect",
    long_description_content_type="text/markdown",
    url="https://github.com/vancy12/wifi-password-finder.git",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["wifi-password = wifi_password.wifi_password:main"]},
    install_requires=["qrcode", "image", "Pillow", "colorama"],
)
