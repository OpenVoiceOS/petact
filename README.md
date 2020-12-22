# OVOS skill installer

download, extract and check for changes in github mycroft skills

## Usage

Skills can be installed from github branches or releases, from .zip or .tar.gz files

```python
from ovos_skill_installer import install_skill

folder = "extract_here"

# using github branches

url = "https://github.com/MycroftAI/skill-playback-control/archive/20.02.zip"
updated = install_skill(url, folder, "skill-playback.zip")
assert updated == True

# should remove files from above
url = "https://github.com/MycroftAI/skill-playback-control/archive/20.08.zip"
updated = install_skill(url, folder, "skill-playback.zip")
assert updated == True

updated = install_skill(url, folder, "skill-playback.zip")
assert updated == False


# Using github releases

url = "https://github.com/JarbasSkills/skill-wolfie/archive/v0.1.tar.gz"
updated = install_skill(url, folder, "skill-wolfie.tar.gz")
assert updated == True

# should remove files from above
url = "https://github.com/JarbasSkills/skill-wolfie/archive/v0.1UPDATE_TEST.tar.gz"
updated = install_skill(url, folder, "skill-wolfie.tar.gz")
assert updated == True

updated = install_skill(url, folder, "skill-wolfie.tar.gz")
assert updated == False
```


## Installation

```bash
pip3 install ovos_skill_installer
```
