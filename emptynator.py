import os
import argparse


def deleteEmptyFoldersRecursively(dir):
    for file in os.scandir(dir):
            if file.is_dir():
                path=file.path
                if not len(os.listdir(path)):
                     os.rmdir(path)
                     print(file.name,"is removed")
                else:
                     deleteEmptyFolders(path)

def deleteEmptyFolders(dir):
    for file in os.scandir(dir):
            if file.is_dir():
                path=file.path
                if not len(os.listdir(path)):
                     os.rmdir(path)
                     print(file.name,"is removed")
               
def deleteEmptyFiles(dir):
     for file in os.scandir(dir):
          if file.is_file():
            path=file.path
            with open(path,"r"):
                 if not os.path.getsize(path):
                      os.remove(path)
                      print(file.name,"is removed")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", help="Path to the source directory")
    args = parser.parse_args()
    dir = args.source_dir
    print("This script is not going to destroy you career dw")
    deleteEmptyFiles(dir)
    print("Do you want to delete empty folders recursively? y/n?")
    ans=input().strip().upper()
    if (ans=="Y" or ans=="YES"or ans=="YE"):
      print("Warned yaa")
      deleteEmptyFoldersRecursively(dir)
      exit()
    deleteEmptyFolders(dir)
    exit()



if __name__ == "__main__":
    main()






