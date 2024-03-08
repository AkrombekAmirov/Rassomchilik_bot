from os.path import join, dirname


async def get_files():
    return join(dirname(__file__), "person.xlsx")
