'''#AsyncIO#'''

import time
import asyncio
import requests


async def fxn1():

    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram1.jpg", "wb").write(response.content)
    print("fxn 1");
    return "harry";
async def fxn2():
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)
    print("fxn 2");
    
async def fxn3():
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram3.jpg", "wb").write(response.content)
    print("fxn 3");

async def fxn4():

    l=await asyncio.gather(
        fxn1(),
        fxn2(),
        fxn3(),
    )
    print(l);

    # task=asyncio.create_task(fxn1());
    # # await fxn1();
    # await fxn2();
    # await fxn3();

asyncio.run(fxn4());

    