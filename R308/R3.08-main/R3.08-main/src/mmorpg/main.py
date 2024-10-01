from guerrier import Guerrier
from mage import Mage

def main():
    marius = Mage("marius", 15)
    print(marius)
    valentin = Guerrier("valentin", 10)
    print(valentin)
    print(marius.combat(valentin))
if __name__ == "__main__":
    main()