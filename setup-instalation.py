import os
import subprocess
from contextlib import suppress

os.chdir("/home/studio-lab-user")  

def run_command(command, message):
    print(f"Please wait, {message} is loading...")
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{message} completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {message} failed with the following output:\n{e.stderr.decode('utf-8')}")

commands = [
    ('conda install conda -y', 'Conda'),
    ('conda update -n base conda -y', 'Update'),
    ('conda install -n base python=3.10 -y', 'Python'),
    ('conda install -q -y glib gxx_linux-64 ffmpeg imageio imageio-ffmpeg av gst-libav psutil gperftools aria2 gdown pydantic', 'glib')
]

def download_ext(command):
    print("Downloading Extensions")
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Extension downloaded successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Extension download failed with the following output:\n{e.stderr.decode('utf-8')}")

extensions = [
    'git clone https://github.com/NoCrypt/sd-fast-pnginfo.git',
    'git clone https://github.com/etherealxx/batchlinks-webui.git',
    'git clone https://github.com/Bing-su/adetailer.git',
    'git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git',
    'git clone https://github.com/BlafKing/sd-civitai-browser-plus.git',
    'git clone https://github.com/zanllp/sd-webui-infinite-image-browsing.git',
    'git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111.git',
    'git clone https://github.com/uwidev/sd_extension-prompt_formatter',
    'git clone https://github.com/picobyte/stable-diffusion-webui-wd14-tagger',
    'git clone https://github.com/mcmonkeyprojects/sd-dynamic-thresholding',
    'git clone https://github.com/hako-mikan/sd-webui-supermerger',
    'git clone https://github.com/huchenlei/sd-webui-openpose-editor',
    'git clone https://github.com/Mikubill/sd-webui-controlnet',
    'git clone https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111',
    'git clone https://github.com/continue-revolution/sd-webui-animatediff',
    'git clone https://github.com/hako-mikan/sd-webui-regional-prompter',
    'git clone https://github.com/catppuccin/stable-diffusion-webui',
    'git clone https://github.com/thomasasfk/sd-webui-aspect-ratio-helper'

]

for command, message in commands:
    run_command(command, message)

os.chdir('/home/studio-lab-user/stable-diffusion-webui-sage/extensions')

for extension in extensions:
    download_ext(extension)