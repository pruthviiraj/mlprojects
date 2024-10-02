from setuptools import find_packages, setup
hype_e_dot = '-e .'

# Function to install requirements.txt 
def get_requirements(file_path:str)->list[str]:

    '''
    this function will run the list of requirements
    '''
    requiremnets=[]
    with open(file_path) as file_obj:
        requiremnets = file_obj.readlines()
        requiremnets = [req.replace("\n", " ") for req in requiremnets]

        if hype_e_dot in requiremnets:
            requiremnets.remove(hype_e_dot)

    return requiremnets

setup(
    name = 'mlprojects',
    version='0.0.1',
    author='Pruthvi',
    author_email='pruthvirajpudi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)