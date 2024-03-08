from distutils.core import setup
from distutils.command.clean import clean
from distutils.command.install import install

requirements = [
    'scikit-learn==1.4.*',
    'numpy==1.26.*',
    'scipy==1.12.*'
]


class CleanInstall(install):
    # Calls the default run command, then deletes the build area
    # (equivalent to "setup clean --all").
    def run(self):
        install.run(self)
        c = clean(self.distribution)
        c.all = True
        c.finalize_options()
        c.run()


setup(
    name="git_cluster",
    version="1.0",
    author="gaozhangyang",
    author_email="gaozhangyang@westlake.edu.cn",
    description="GIT: Clustering Based on Graph of Intensity Topology",
    packages=['git_cluster'],
    install_requires=requirements,
    # egg_base='/tmp',
    cmdclass={'install': CleanInstall}
)
