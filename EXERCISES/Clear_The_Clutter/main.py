# import os;

# folder = os.listdir("clutter")
# for i in range(len(folder)):
#      a=i;
#      file=folder[i];
#      os.rename(f"clutter/{file}",f"clutter/{a+1}.png");



# ////////////////////////////////////////////////////

import os

files = os.listdir("HarryClutter")
i = 1
for file in files:
  if file.endswith(".jpg"):
    print(file)
    os.rename(f"HarryClutter/{file}", f"HarryClutter/{i}.png")
    i = i + 1;