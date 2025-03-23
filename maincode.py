import time
import shutil
from pathlib import Path
import os
import subprocess
import sys
import datetime


class Color:
	BLACK          = '\033[30m'
	RED            = '\033[31m'
	GREEN          = '\033[32m'
	YELLOW         = '\033[33m'
	BLUE           = '\033[34m'
	MAGENTA        = '\033[35m'
	CYAN           = '\033[36m'
	WHITE          = '\033[37m'
	COLOR_DEFAULT  = '\033[39m'
	BOLD           = '\033[1m'
	UNDERLINE      = '\033[4m'
	INVISIBLE      = '\033[08m'
	REVERCE        = '\033[07m'
	BG_BLACK       = '\033[40m'
	BG_RED         = '\033[41m'
	BG_GREEN       = '\033[42m'
	BG_YELLOW      = '\033[43m'
	BG_BLUE        = '\033[44m'
	BG_MAGENTA     = '\033[45m'
	BG_CYAN        = '\033[46m'
	BG_WHITE       = '\033[47m'
	BG_DEFAULT     = '\033[49m'
	RESET          = '\033[0m'


appdata_path = os.path.expandvars(r"%APPDATA%")
mainfolder_path = os.path.join(appdata_path, "mcjemodpkgrfiles", "mu")
allorom = coworag = 'fake'

while True:
   if os.path.isdir(mainfolder_path):
          break
   
   else:
          os.makedirs(mainfolder_path)
          break


time.sleep(0.6)
print("Welcome to mcjeModpkgr[Beta-v0.9a] by ika3")
print()
time.sleep(0.3)
print("You can Create new launch-config or Append mods/shaderpacks to current launch-config")
time.sleep(0.4)
print("or Check the lists of things or Delete folder/files or Get folder-path or Rename folder or Get files from packaged folder .")
time.sleep(0.8)
print()


while True:
    print("You can select option from the following lists. Please select one option required.")
    in1 = input("Create[C] Append[A] Lists[L] Delete[D] Getpath[GP] Rename-folder[RN] Getfile[GF] : ").strip().lower()
    time.sleep(0.4)

    if in1 == 'c':
        time.sleep(0.3)

        while True:
            if coworag == 'o':
                shutil.rmtree(fullc_path)
                print()
                time.sleep(0.4)
                print (f"[Create] WARNING!! Your current {clfname} folder is overwritten!!")
                break

            else:
             print()
             time.sleep(0.1)
             clfname = input("[Create] Enter folder name : ").strip().lower()
             fullc_path = os.path.join(mainfolder_path, clfname)
             if os.path.isdir(fullc_path):
                 time.sleep(0.3)
                 print()
                 print(f"[Create] The {clfname} folder is already in use.") 

                 while True:
                     coworag = input("[Create] Overwrite[O] or Enter folder name again[E] : ").strip().lower()
                     if coworag == 'o' or 'e':
                      break
             
                     else:
                      time.sleep(0.2)
                      print("[Create] Wrong input! Try again.")


             else:
                break
        
        while True:
         print()
         time.sleep(0.2)
         allorom = input("[Create] Only shaderpacks[S] or Only mods[M] or All files(for modpacks)[A] ? : ").strip().lower()

         if allorom == 'm':
             modpath = os.path.join(fullc_path, "mods") 
             shutil.copytree("./fls", modpath)
             break
         
         elif allorom == 'a':
             shutil.copytree("./fls", fullc_path)
             break
         
         elif allorom == 's':
             sppath = os.path.join(fullc_path, "shaderpacks")
             shutil.copytree("./fls", sppath)

         else:
            time.sleep(0.2)
            print("Wrong input! Try again.")
            time.sleep(0.2)
 
        time.sleep(1.2)
        print("Successfully packaged.")
        time.sleep(0.4)
        print()
        print("Do you want to delete files in fls folder automatically?")
        time.sleep(0.2)

        while True:
           delorn = input("Delete[D] or not[N] : ").strip().lower()

           if delorn == 'n':
              break
           
           elif delorn == 'd':
              shutil.rmtree("./fls")
              os.makedirs("./fls", exist_ok=True)
              print()
              time.sleep(0.7)
              print("Deleted.")

              break
           
           else:
              print("Wrong input! Try again.")

        print()
        time.sleep(0.4)
        crspcheck = os.path.join(fullc_path, "shaderpacks")

        if os.path.isdir(crspcheck):
         print("Here is your folder path. [Already copied to clipboard]")
         print (f"{fullc_path}")
         time.sleep(0.2)
         print()
         subprocess.run("clip", input=fullc_path, text=True)
         print("Have fun to play modded MCJE and Thank you for using my script!")
         time.sleep(1.2)
         print()
         print()
         print("You can close this window.")
         time.sleep(30)
         sys.exit()

        else:
         os.makedirs(crspcheck, exist_ok=True)
         print("Here is your folder path. [Already copied to clipboard]")
         print (f"{fullc_path}")
         time.sleep(0.2)
         print()
         subprocess.run("clip", input=fullc_path, text=True)
         print("Have fun to play modded MCJE and Thank you for using my script!")
         time.sleep(1.2)
         print()
         print()
         print("You can close this window.")
         time.sleep(30)
         sys.exit()
 

    elif in1 == 'a':
       while True:
          in2 = input("Append mods[AM] or Append shaderpacks[AS] : ").strip().lower()
    
          if in2 == 'am':
            while True:   
             print()
             time.sleep(0.2)
             apfile = input("[Append] Enter folder name :").strip().lower()
             time.sleep(0.4)
             print()
             full_path_a = os.path.join(appdata_path, "mcjemodpkgrfiles", apfile)
             full_path_a_m = os.path.join(appdata_path, "mcjemodpkgrfiles", apfile, "mods")
             if os.path.isdir(full_path_a):
              print("[Append] We only support to append only mods in this option.")

              while True:
                time.sleep(0.3)
                aprly = input("[Append] Are you sure to append, yes[Y] or no[N]? :").strip().lower()
            
                if aprly == 'y':
                    shutil.copytree("./fls", full_path_a_m, dirs_exist_ok=True)
                    time.sleep(0.2)

                    print("Successfully appended.")
                    print()
                    time.sleep(0.2)
                    print("Do you want to delete files in fls folder automatically?")

                    while True:
                        time.sleep(0.2)
                        delorna = input("Delete[D] or not[N] :").strip().lower()

                        if delorna == 'n':
                            break
            
                        elif delorna == 'd':
                            shutil.rmtree("./fls")
                            os.makedirs("./fls", exist_ok=True)
                            print()
                            time.sleep(0.2)
                            print("Deleted.")
                            time.sleep(0.2)
                            break
                        
                        else:
                         time.sleep(0.2)
                         print("Wrong input! Try again.")
                         time.sleep(0.2)
                    
                    time.sleep(0.2)
                    print("Here is your folder path. [Already copied to clipboard]")
                    time.sleep(0.2)
                    print (f"{full_path_a}")
                    print()
                    time.sleep(0.2)
                    subprocess.run("clip", input=full_path_a, text=True)
                    print("Have fun to play modded MCJE and Thank you for using my script!")
                    time.sleep(1.2)
                    print()
                    print()
                    print("You can close this window.")
                    time.sleep(30)
                    sys.exit()

                elif aprly == 'n':
                    print()
                    time.sleep(0.5)
                    print("The window is going to close.")
                    time.sleep(2)
                    sys.exit()

             else:
                print("[Append] Wrong input or the Folder does not exist. Try again.")   


          elif in2 == 'as':
            while True:   
             print()
             time.sleep(0.2)
             apfile2 = input("[Append] Enter folder name :").strip().lower()
             time.sleep(0.4)
             print()
             full_path_as = os.path.join(appdata_path, "mcjemodpkgrfiles", apfile2)
             full_path_as_m = os.path.join(appdata_path, "mcjemodpkgrfiles", apfile2, "shaderpacks")
             if os.path.isdir(full_path_as):
                    # You found the easter egg!
              print("[Append] We only support to append only shaderpacks in this option.")

              while True:
                time.sleep(0.3)
                aprly = input("[Append] Are you sure to append, yes[Y] or no[N]? :").strip().lower()
            
                if aprly == 'y':
                    shutil.copytree("./fls", full_path_as_m, dirs_exist_ok=True)
                    time.sleep(0.2)

                    print("Successfully done.")
                    print()
                    time.sleep(0.2)
                    print("Do you want to delete files in fls folder automatically?")

                    while True:
                        time.sleep(0.2)
                        delorna = input("Delete[D] or not[N] :").strip().lower()

                        if delorna == 'n':
                            break
            
                        elif delorna == 'd':
                            shutil.rmtree("./fls")
                            os.makedirs("./fls", exist_ok=True)
                            print()
                            time.sleep(0.2)
                            print("Deleted.")
                            time.sleep(0.2)
                            break
                        
                        else:
                         time.sleep(0.2)
                         print("Wrong input! Try again.")
                         time.sleep(0.2)
                    
                    time.sleep(0.2)
                    print("Here is your folder path. [Already copied to clipboard]")
                    time.sleep(0.2)
                    print (f"{full_path_as}")
                    print()
                    time.sleep(0.2)
                    subprocess.run("clip", input=full_path_as, text=True)
                    print("Have fun to play modded MCJE and Thank you for using my script!")
                    time.sleep(1.2)
                    print()
                    print()
                    print("You can close this window.")
                    time.sleep(30)
                    sys.exit()

                elif aprly == 'n':
                    print()
                    time.sleep(0.5)
                    print("The window is going to close.")
                    time.sleep(2)
                    sys.exit()

             else:
                print("[Append] Wrong input or the Folder does not exist. Try again.") 

          else:
             time.sleep(0.35)
             print("[Append] Wrong input! Try again.") 
             print()

    elif in1 == 'l':
        print()
        
        while True:
           whichlistis = input("[Lists] Which list do you want to check, folders[F] or mods[M] or shaderpacks[S] ? : ").strip().lower()

           if whichlistis == 'f':
             time.sleep(0.3)
             print()
             print()
             print("[Lists] Here's the list of folders.")
             print()
             dirfl1 = [
             f for f in os.listdir(mainfolder_path) if os.path.isdir(os.path.join(mainfolder_path, f))
             ]
             for dirfl2 in dirfl1:
              print(dirfl2)
             print()
             print()
             print()
             break
           
           elif whichlistis == 'm':
              time.sleep(0.3)
              print()
              while True:
               modlistfolder_name = input("[Lists] Enter folder name : ").strip().lower()
               modlistfolder_full_path = os.path.join(mainfolder_path, modlistfolder_name, "mods")
               print()

               if os.path.isdir(modlistfolder_full_path):
                       time.sleep(0.5)
                       print()
                       print()
                       print(f"[Lists] Here's the list of mods in {modlistfolder_name} folder.")
                       print()
                       dirmd1 = [
                       f for f in os.listdir(modlistfolder_full_path) if os.path.isfile(os.path.join(modlistfolder_full_path, f))
                       ]
                       for dirmd2 in dirmd1:
                         print(dirmd2)
                       print()
                       print()
                       print()
                       break
                     
               else:
                  print("[Lists] Wrong input or the Folder does not exist. Try again.")
                  time.sleep(0.3)
                  continue
              break
                  
                     
           elif whichlistis == 's':
             time.sleep(0.3)
             print()
             while True:
                 splistfolder_name = input("[Lists] Enter folder name : ").strip().lower()
                 splistfolder_full_path = os.path.join(mainfolder_path, splistfolder_name, "shaderpacks")
                 print()

                 if os.path.isdir(splistfolder_full_path):
                       time.sleep(0.3)
                       print()
                       print()
                       print(f"[Lists] Here's the list of mods in {modlistfolder_name} folder.")
                       print()
                       dirsp1 = [
                       f for f in os.listdir(splistfolder_full_path) if os.path.isfile(os.path.join(splistfolder_full_path, f))
                       ]
                       for dirsp2 in dirsp1:
                         print(dirsp2)
                       print()
                       print()
                       print()
                       break
                     
                 else:
                  print("[Lists] Wrong input or the Folder does not exist. Try again.")
                  time.sleep(0.3)
                  continue
             break


    elif in1 == 'd':
        while True:
          time.sleep(0.5)
          print()
          delfolder_name = input("[Delete] Enter folder name : ").strip().lower()
          delfolder_path = os.path.join(mainfolder_path, delfolder_name)

          if os.path.isdir(delfolder_path):
             while True:
                time.sleep(0.4)
                deltype_0 = input("[Delete] Delete folder[F] or Delete mods[M] or Delete shaderpacks[S] : ").strip().lower()
                if deltype_0 == 'f' or 'm' or 's':
                   break
                  
                else: 
                   time.sleep(0.4)
                   print("[Delete] Wrong input! Try again.")
                   continue
            
             if deltype_0 == 'f':
                  time.sleep(1.2)
                  delrusure = input('\033[31m'+f"[Delete] Are you sure to delete {delfolder_name} folder, Delete[DELETE] or Cancel[C]? : "+'\033[0m').strip().lower()
                  if delrusure == 'delete':
                     print()
                     shutil.rmtree(delfolder_path)
                     time.sleep(0.6)
                     print("[Delete] Successfully deleted.")
                     break
                  elif delrusure == 'c':
                     print()
                     time.sleep(0.2)
                     print("[Delete] Cancelled!")
                     break
                  else:
                     time.sleep(0.3)
                     print("[Delete] Wrong input! Try again.")
                     print()

             elif deltype_0 == 'm':
                time.sleep(0.7)
                delfolder_mods_path = os.path.join(delfolder_path, "mods")
                print()
                print()
                print(f"Here's the list of mods in {delfolder_name}.")
                print()
                dir_del_mods_1 = [
                f for f in os.listdir(delfolder_mods_path) if os.path.isdir(os.path.join(delfolder_mods_path, f))
                ]
                for dir_del_mods_2 in dir_del_mods_1:
                   print(f"\033[38;2;245;130;25m{dir_del_mods_2}\033[0m");
                print()
                print("Enter that a mod name to delete the mod.")
                print("When the removal is complete, enter [EXIT] to exit.")
                print("To see the list of mods, enter [MODSLIST].")
                print()
                print()
                while True:
                   del_mods_name = input("Enter a mod name or command. : ").strip()
                   time.sleep(0.4)

                   if del_mods_name.lower() == 'exit':
                      print("Thank you for using my script!")
                      time.sleep(2)
                      print()
                      print("You can close this window.")
                      time.sleep(30)
                      sys.exit()
                   
                   elif del_mods_name.lower() == 'modslist':
                      print()
                      print()
                      print(f"Here's the current list of mods in {delfolder_name}.")
                      print()
                      dir_del_mods_1 = [
                      f for f in os.listdir(delfolder_mods_path) if os.path.isdir(os.path.join(delfolder_mods_path, f))
                      ]
                      for dir_del_mods_2 in dir_del_mods_1:
                         print(f"\033[38;2;245;130;25m{dir_del_mods_2}\033[0m");
                      print()
                      print()
                      continue
                   
                   else:
                      del_mods_file_full_path = os.path.join(delfolder_mods_path, del_mods_name)
                      if os.path.isfile(del_mods_file_full_path):
                         os.remove(del_mods_file_full_path)
                         print("Removed "+f"\033[38;2;255;198;33m{del_mods_name}\033[0m"+" successfully.");
                         print()
                         continue
                      
                      else:
                         print("The file not found. Try again.")
                         print()
                         continue

          else:
             time.sleep(0.2)
             print("[Delete] Wrong input or the Folder does not exist. Try again.")
             print()
             time.sleep(0.2)
             continue
          
          break
            
        print()
        time.sleep(0.5)
        print("The window is going to close")
        time.sleep(3)
        sys.exit()

    elif in1 == 'gp':
       while True:
          time.sleep(0.5)
          print()
          gpfoldername = input("[Getpath] Enter folder name : ").strip().lower()
          gp_path0 = os.path.join(mainfolder_path, gpfoldername)
          if os.path.isdir(gp_path0):
             print()
             print()
             time.sleep(0.9)
             print("Here is your folder path. [Already copied to clipboard]")
             time.sleep(0.3)
             print (f"{gp_path0}")
             print()
             time.sleep(0.2)
             subprocess.run("clip", input=gp_path0, text=True)
             print("Have fun to play modded MCJE and Thank you for using my script!")
             time.sleep(1.2)
             print()
             print()
             print("You can close this window.")
             time.sleep(30)
             sys.exit()

          else:
             time.sleep(0.2)
             print("[Getpath] Wrong input or the Folder does not exist. Try again.")
        
    
    elif in1 == 'rn':
       while True:
          time.sleep(0.4)
          print()
          rnfoldername_c = input("[Rename] Enter current name of the folder you want to rename : ").strip().lower()
          rnfull_path_c = os.path.join(mainfolder_path, rnfoldername_c)
          if os.path.isdir(rnfull_path_c):
             print()
             time.sleep(0.4) 
             rnfoldername_n = input("[Rename] Enter the new folder name : ").strip().lower()
             rnfull_path_n0 = os.path.join(mainfolder_path, rnfoldername_n)
             while True:
              if os.path.isdir(rnfull_path_n0):
                print()
                time.sleep(0.25)
                print("[Rename] The folder name is already in use.")

                while True:
                 time.sleep(0.2)
                 rnowornot = input(f"[Rename] Overwrite {rnfoldername_n} folder[O] or Enter the new folder name again[E] : ").strip().lower()

                 if rnowornot == 'o' or 'e':
                    time.sleep(0.2)
                    print()
                    break
                 
                 else:
                    time.sleep(0.15)
                    print("[Rename] Wrong input! Try again.")
                    print()

                if rnowornot == 'o':
                   break

                else:
                   continue

              else:
                 break
              
             os.rename(rnfull_path_c, rnfull_path_n0)
             time.sleep(0.6)
             print()
             print("Renamed folder.")
             print()
             time.sleep(0.3)
             print("Here is your new folder path. [Already copied to clipboard]")
             print (f"{rnfull_path_n0}")
             time.sleep(0.2)
             print()
             subprocess.run("clip", input=rnfull_path_n0, text=True)
             print("Have fun to play modded MCJE and Thank you for using my script!")
             time.sleep(1.2)
             print()
             print()
             print("You can close this window.")
             time.sleep(30)
             sys.exit()


          elif in1 == 'gf':
             print()
             while True:
                time.sleep(0.5)
                gffoldername = input("[Getfile] Enter name of the folder containing the file you want to retrieve : ").strip().lower()
                print()
                gffull_path = os.path.join(mainfolder_path, gffoldername)
                if os.path.isdir(gffull_path):
                   while True:
                      gf_wf = input("[Getfile] All files[A] or Only mods[M] or Only shaderpacks[S] : ").strip().lower()
                      print()
                      gf_timenow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                      gf_2_dirname = (f"{gffoldername}-{gf_wf}_archive_{gf_timenow}")
                      gf_2_dir = os.path.join("./fls", "archive", gf_2_dirname)
                      if gf_wf == 'a':
                         shutil.copytree(gffull_path, gf_2_dir, dirs_exist_ok=True)
                         break

                      elif gf_wf == 'm':
                         gffull_path_m = os.path.join(gffull_path, "mods")
                         shutil.copytree(gffull_path_m, gf_2_dir, dirs_exist_ok=True)
                         break

                      elif gf_wf == 's':
                         gffull_path_s = os.path.join(gffull_path, "shaderpacks")
                         shutil.copytree(gffull_path_s, gf_2_dir, dirs_exist_ok=True)
                         break

                      else:
                         print("[GetFile] Wrong input! Try again.")

                   time.sleep(1.5)
                   print(f"Successfully copied files in {gf_2_dirname} in archive folder.")
                   time.sleep(1.2)
                   print()
                   print()
                   print("You can close this window.")
                   time.sleep(30)
                   sys.exit()


                else:
                   print("[Getfile] Wrong input or the folder does not exist. Try again.")
                   print()
             


          else:
             time.sleep(0.3)
             print("[Rename] Wrong input or the Folder does not exist. Try again.")


    else:
        time.sleep(0.2)
        print("Wrong input! Try again.")
        time.sleep(0.9)
        print()