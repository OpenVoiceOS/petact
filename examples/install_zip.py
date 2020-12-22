from ovos_skill_installer import install_skill

# using github branches


url = "https://github.com/MycroftAI/skill-playback-control/archive/20.02.zip"
folder = "installed_stuff"
updated = install_skill(url, folder, "skill-playback.zip")
assert updated == True

# should remove files from above
url = "https://github.com/MycroftAI/skill-playback-control/archive/20.08.zip"
updated = install_skill(url, folder, "skill-playback.zip")
assert updated == True

updated = install_skill(url, folder, "skill-playback.zip")
assert updated == False