from ovos_skill_installer import install_skill

# Using github releases


url = "https://github.com/JarbasSkills/skill-wolfie/archive/v0.1.tar.gz"
folder = "installed_stuff"
updated = install_skill(url, folder, "skill-wolfie.tar.gz")
assert updated == True

# should remove files from above
url = "https://github.com/JarbasSkills/skill-wolfie/archive/v0.1UPDATE_TEST.tar.gz"
updated = install_skill(url, folder, "skill-wolfie.tar.gz")
assert updated == True

updated = install_skill(url, folder, "skill-wolfie.tar.gz")
assert updated == False