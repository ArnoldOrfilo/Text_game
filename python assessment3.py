     #    ######   #     #  #####  #       ####
    # #   #     #  # #   # #     # #       #   #
   #   #  ######   #  #  # #     # #       #    #
  ####### # #      #   # # #     # #       #    #
 #       ##  #     #    ## #     # #       #   #
#         #    # ###     #  #####  ####### ####



import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import random

##have to change the healing pad in the bag. should be used in the bag

class User:

    name=""
    health_=100
    point_=0
    money=random.randint(50,310)+1000
    bag=[[],[],[],[]] #weapon, armour, healing pad, key 
    attack=3
    defense=0
    using={'Weapon':'Fist', 'Armour':'None'}
        
class shop:

    weapon=[]
    armour=[]
    healing_pad=[]
    key=[]
    all_items=[]
    

class weapon:

    def __init__(weapon,name,damage,price,stock): # initialise 
        weapon.name=name
        weapon.damage=damage
        weapon.price=price
        weapon.stock=stock

class healing_pad:

    def __init__(pad,name,power,price,stock):
        pad.name=name
        pad.power=power
        pad.price=price
        pad.stock=stock


class armour:

    def __init__(armour,name,duability,price,stock):
        
        armour.name=name
        armour.duability=duability
        armour.price=price
        armour.stock=stock


class key:

    def __init__(key,code,price):
        key.name='key'
        key.stock=1
        key.code=code
        key.price=price

class rooms:

    def __init__(room_):

        room_.enermy={'Name':'','Damage':0,'Health':100}
        room_.treasure={'Exist':False,'Code':0, 'Point':0}
        room_.weapons={'Name':'','Damage':0,'Price':0,'Stock':1}
        room_.healing_pad_={'Exist':False,'Stock':0}
        room_.keys={'Exist':False,'Code':0,'Price':0}
        room_.point=0
        room_.money=0




def extract_information_rooms(room_info):

    


    room=rooms()

    for i in range(len(room_info)):
        if '# Enemy' in room_info[i]:
            room_enemy_file=room_info[i+1].rstrip()
            room_enemy_file=room_enemy_file.split(',')
            room.enermy['Name']=room_enemy_file[0]
            room.enermy['Damage']=int(room_enemy_file[1])
            room.enermy['Health']=int(room_enemy_file[2])

        elif '# Point' in room_info[i]:
            room.point=int(room_info[i+1].rstrip())

        elif '# Weapon' in room_info[i]:
            room_weapon_file=room_info[i+1].rstrip()
            room_weapon_file=room_weapon_file.split(',')
            room.weapons['Name']=room_weapon_file[0]
            room.weapons['Damage']=int(room_weapon_file[1])
            room.weapons['Price']=int(room_weapon_file[2])

        elif '# Money' in room_info[i]:
            room.money=int(room_info[i+1].rstrip())

        elif '# Healing' in room_info[i]:
            room.healing_pad_['Exist']=True
            room.healing_pad_['Stock']=int(room_info[i+1].rstrip())

        elif '# Key' in room_info[i]:
            room.keys['Exist']=True
            room_key_file=room_info[i+1].rstrip()
            room_key_file=room_key_file.split(',')
            room.keys['Code']=int(room_key_file[0])
            room.keys['Price']=int(room_key_file[1])


        elif '# Treasure' in room_info[i]:
            room.treasure['Exist']=True
            room_treasure_file=room_info[i+1].rstrip()
            room_treasure_file=room_treasure_file.split(',')
            room.treasure['Code']=int(room_treasure_file[0])
            room.treasure['Point']=int(room_treasure_file[1])


    return room


def extract_and_implement_items_shop():
    shop_f=open('shop.txt','r')
    shop_inventory=shop_f.readlines()
    shop_f.close()

    

    weapon_description_set=[] #raw data from file. ['weapon name, weapon damage, weapon price','weapon name, weapon damage, weapon price']
    key_description_set=[] 
    healing_pad_description_set=[]#[' health +50, price 100', '5']
    armour_description_set=[]


    weapon_info_set=[] #processed data from file. [['weapon name', 'weapon damage', 'weapon price'],['weapon name', 'weapon damage', 'weapon price']]
    armour_info_set=[]
    healing_pad_info_set=[]
    key_info_set=[]




   
    counter=0


    for n in shop_inventory:
        n=n.rstrip() # rstrip() can delete element at the end of a string. If don't fill in the (), it will delete space and \n by default.

        try:
            if n[0]+n[1]+n[2]+n[3]+n[4]+n[5]=="weapon" or n[0]+n[1]+n[2]+n[3]+n[4]+n[5]=="Weapon":
                
                temp_line=''
                valid=False

                for i in range(len(n)):

                    if n[i]==":":
                        valid=True

                    elif valid==True:
                        temp_line+=n[i]
                        
                    
                weapon_description_set.append(temp_line)

                counter+=1
            

        except IndexError:
            counter+=1
            continue
            

        try:

            if n[0]+n[1]+n[2]=="key" or n[0]+n[1]+n[2]=="Key":
                temp_line=''
                valid=False

                for i in range(len(n)):

                    if n[i]==":":
                        valid=True

                    elif valid==True:
                        temp_line+=n[i]

                key_description_set.append(temp_line)
                counter+=1
                

        except IndexError:
            counter+=1
            continue
        


        try:
            if n[0]+n[1]+n[2]+n[3]=="Heal":
                

                temp_line=''
                valid=False
                
                for i in range(len(n)):

                    if n[i]==":":
                        valid=True

                    elif valid==True:
                        temp_line+=n[i]

                healing_pad_description_set.append(temp_line)
                counter+=1
                
                


        except IndexError:
            counter+=1
            continue
        
        try:
            if n[0]+n[1]+n[2]+n[3]+n[4]+n[5]=="armour" or n[0]+n[1]+n[2]+n[3]+n[4]+n[5]=="Armour":
                armour_description_set.append(n)
                counter+=1

        except IndexError:
            counter+=1
            continue
        
        




    for n in weapon_description_set:
        
        temp_info=n.split(",")
        weapon_info_set.append(temp_info)
        

    for temp_object in weapon_info_set:
        temp_weapon=weapon(temp_object[0],int(temp_object[1]),int(temp_object[2]),1)
        store.weapon.append(temp_weapon)
        store.all_items.append(temp_weapon)
        





    for m in armour_description_set:
        
        temp_info_armour=m.split(",") # if there's a ',' then temp_info is a list
        armour_info_set.append(temp_info_armour)


    for temp_object_armour in armour_info_set:

        temp_armour_attribute=temp_object_armour[0].split(":") #name and duability

        temp_armour=armour(temp_armour_attribute[0],int(temp_armour_attribute[1]),int(temp_object_armour[1]),1)
        store.armour.append(temp_armour)
        store.all_items.append(temp_armour)



    for h in healing_pad_description_set:
        temp_info_healing_pad=h.split(",")
        healing_pad_info_set.append(temp_info_healing_pad)
    
    

    for temp_attribute_healing_pad in healing_pad_info_set:
   
        healing_pad1=healing_pad('healing pad',int(temp_attribute_healing_pad[0]),int(temp_attribute_healing_pad[1]),int(temp_attribute_healing_pad[2]))
        store.healing_pad.append(healing_pad1)
        store.all_items.append(healing_pad1)



    



    for j in key_description_set:
        
        
        temp_info=j.split(",")
        key_info_set.append(temp_info)

    for o in key_info_set:

        temp_key=key(int(o[0]),int(o[1]))
        store.key.append(temp_key)
        store.all_items.append(temp_key)
    


def first_page_frames_pack():# prompt user for username #frame_prompt_username

    global frame_prompt_username
    frame_prompt_username=tkinter.Frame(window1)# Enter user name
    # below are for username entry
    prompt_for_name=tkinter.Label(frame_prompt_username,text="Please enter your username: ")
    prompt_for_name.grid(row=0,column=0)

    global name_entrance #cross functions
    name_entrance=tkinter.Entry(frame_prompt_username)
    name_entrance.grid(row=0,column=1)


    confirm_button=tkinter.Button(frame_prompt_username,text="Submit",command=page_swtich1)
    confirm_button.grid(row=0,column=2)
    frame_prompt_username.pack(expand=True)# fill the spare space of window1 to make content in the center




def information_frame_pack(): # frame_informations 

    global frame_informations,money,points,health,money,arm_using,player_stat
    frame_informations=tkinter.Frame(window1) # health, money and points
    name=tkinter.Label(frame_informations,text=player.name)
    name.grid(row=0,column=0,padx=10, pady=10)
    health=tkinter.Label(frame_informations,text="Health: "+str(player.health_))
    health.grid(row=0,column=1,padx=10, pady=10)
    money=tkinter.Label(frame_informations,text="Money: "+str(player.money))
    money.grid(row=0,column=2,padx=10, pady=10)
    points=tkinter.Label(frame_informations,text="Points: "+str(player.point_))
    points.grid(row=0,column=3,padx=10, pady=10)
    arm_using=tkinter.Label(frame_informations,text='Weapon: '+player.using['Weapon']+'    Armour: '+player.using['Armour'])
    arm_using.grid(row=0,column=4,padx=10, pady=10)
    player_stat=tkinter.Label(frame_informations,text='Attack: '+str(player.attack)+'      Defense: '+str(player.defense))
    player_stat.grid(row=0,column=5,padx=10, pady=10)


    frame_informations.pack()

    

def configure_armed_gear_string():


    arm_using.configure(text='Weapon: '+player.using['Weapon']+'    Armour: '+player.using['Armour'])
    player_stat.configure(text='Attack: '+str(player.attack)+'      Defense: '+str(player.defense))

        
    
   
            




   



def menu_frame_pack(): #frame buttons
    global frame_buttons
    frame_buttons=tkinter.Frame(window1)

    Button_quit=tkinter.Button(frame_buttons, text="Quit Game", command=quit_game)
    Button_room1=tkinter.Button(frame_buttons,text="Room1",command=page_switch6)
    Button_room2=tkinter.Button(frame_buttons,text="Room2",command=page_switch10)
    Button_room3=tkinter.Button(frame_buttons,text="Room3",command=page__switch11)
    Button_room4=tkinter.Button(frame_buttons,text="Room4",command=page_switch12)
    Button_shop=tkinter.Button(frame_buttons, text="Shop", command=page_switch2)
    Button_bag=tkinter.Button(frame_buttons, text="Bag", command=page_switch4)


    Button_shop.grid(row=0,column=0,padx=10, pady=10)
    Button_bag.grid(row=0,column=1,padx=10, pady=10)
    Button_room1.grid(row=1,column=0,padx=10, pady=10)
    Button_room2.grid(row=1,column=1,padx=10, pady=10)
    Button_room3.grid(row=2,column=0,padx=10, pady=10)
    Button_room4.grid(row=2,column=1,padx=10, pady=10)
    Button_quit.grid(row=3,column=0,padx=10, pady=10)

    frame_buttons.pack()


def shop_frame_pack():# frame_shop   #frame_shop_back_button   #frame_shop_weapon   #frame_shop_sort   #frame_shop_armour  #frame_shop_healing_pad  #frame_shop_buy  #frame_shop_sort_armour #frame_bag_back_button    #frame_bag_weapon

    global frame_shop,frame_shop_back_button,frame_shop_weapon,frame_shop_sort,frame_shop_armour,frame_shop_healing_pad,frame_shop_buy,frame_shop_sort_armour,buy_entrance,frame_shop_key,sell_entrance,frame_shop_sell
    frame_shop=tkinter.Frame(window1) # the welcome text
    frame_shop_back_button=tkinter.Frame(window1)# back to menu button in the shop page
    frame_shop_weapon=tkinter.Frame(window1)# weapons in shop page
    frame_shop_sort=tkinter.Frame(window1) #sort buttons in shop page
    frame_shop_armour=tkinter.Frame(window1)# arnours in shop page
    frame_shop_healing_pad=tkinter.Frame(window1)# healing pad in shop page
    frame_shop_buy=tkinter.Frame(window1) # entrance buying items in shop page
    frame_shop_sort_armour=tkinter.Frame(window1)# sort armour buttons in shop page
    frame_shop_key=tkinter.Frame(window1) #key in shop page
    frame_shop_sell=tkinter.Frame(window1)# button of selling items
    


    #below are shop
    shop_back_to_menu=tkinter.Button(frame_shop_back_button, text="Back", command=page_switch3)
    shop_back_to_menu.grid(row=0,column=0)
    



    #welcome phrase 
    welcome=tkinter.Label(frame_shop,text="Whats up "+player.name+", "+"these are what we have >>                              ")
    welcome.grid(row=0,column=0)
    


    #shop category:weapon
    shop_category_weapon=tkinter.Label(frame_shop,text="\n Weapons:                                                                      ")
    shop_category_weapon.grid(row=1,column=0)

    for i in range(len(store.weapon)):
        shop_weapon1=tkinter.Label(frame_shop_weapon, text=store.weapon[i].name +"         Damage: "+str(store.weapon[i].damage)+"         Price: "+str(store.weapon[i].price)+"         Stock:"+str(store.weapon[i].stock))
        shop_weapon1.grid(row=i,column=0)
        
    shop_sort_by_damage=tkinter.Button(frame_shop_sort, text="Sort by Damage (Descending)",command=weapon_sort_damage) 
    shop_sort_by_damage.grid(row=5,column=0) 
    shop_sort_by_price=tkinter.Button(frame_shop_sort, text="Sort by Price (Ascending)",command=weapon_sort_price)
    shop_sort_by_price.grid(row=5,column=1) 

    
    #shop category:armour
    shop_category_armour=tkinter.Label(frame_shop_armour,text="\n \n Armours:                                                                      ")
    shop_category_armour.grid(row=0,column=0)

    for i in range(len(store.armour)):
        shop_armour1=tkinter.Label(frame_shop_armour, text=store.armour[i].name +"         Duability: "+str(store.armour[i].duability)+"         Price: "+str(store.armour[i].price)+"         Stock:"+str(store.armour[i].stock))
        shop_armour1.grid(row=i+1,column=0)

    sort_armour_by_duability=tkinter.Button(frame_shop_sort_armour,text='Sort by Duability (Descending)', command=armour_sort_duability)
    sort_armour_by_duability.grid(row=0,column=0)
    sort_armour_by_price=tkinter.Button(frame_shop_sort_armour,text='Sort by Price (Ascending)', command=armour_sort_price)
    sort_armour_by_price.grid(row=0,column=1)

    #shop category:healing pad
    for i in range(len(store.healing_pad)):
        shop_category_healing_pad=tkinter.Label(frame_shop_healing_pad,text="\n\n "+store.healing_pad[i].name+"        Health Increase: "+str(store.healing_pad[i].power)+"       Price: "+str(store.healing_pad[i].price)+"        Stock: "+str(store.healing_pad[i].stock))
        shop_category_healing_pad.grid(row=i,column=0)

    #buy function
    space=tkinter.Label(frame_shop_buy,text="\n\n")
    space.grid(row=0,column=0)
    buy_entrance=tkinter.Entry(frame_shop_buy)
    buy_entrance.grid(row=1,column=0)
    buy_button=tkinter.Button(frame_shop_buy,text="Buy", command=purchasing)
    buy_button.grid(row=1,column=1)


    #shop category: key
    for i in range (len(store.key)):
        shop_category_key=tkinter.Label(frame_shop_key,text="\n\n" + store.key[i].name + "        Code: "+str(store.key[i].code)+"        Price: "+str(store.key[i].price)+"        Stock: " + str(store.key[i].stock))
        shop_category_key.grid(row=i,column=0)

    #sell function

    space2=tkinter.Label(frame_shop_sell,text="\n")
    space2.grid(row=0,column=0)
    sell_entrance=tkinter.Entry(frame_shop_sell)
    sell_entrance.grid(row=1,column=0)
    sell_button=tkinter.Button(frame_shop_sell,text="Sell", command=selling)
    sell_button.grid(row=1,column=1)






    frame_shop_back_button.pack()
    frame_shop.pack()
    frame_shop_weapon.pack()
    frame_shop_sort.pack()
    frame_shop_armour.pack()
    frame_shop_sort_armour.pack()
    frame_shop_healing_pad.pack()
    frame_shop_key.pack()
    frame_shop_buy.pack()
    frame_shop_sell.pack()

def bag_frame_pack(): # frame_bag_back_button  #frame_bag_weapon
    
    global frame_bag_back_button,frame_bag_weapon, frame_bag_armour,frame_bag_healingpad,frame_bag_key,frame_bag_use,wear_gear,frame_bag_takeoff,takeoff_armour_button,takeoff_weapon_button

   

    frame_bag_back_button=tkinter.Frame(window1)# back to menu button in bag page
    frame_bag_weapon=tkinter.Frame(window1)# weapon section in bag page
    frame_bag_armour=tkinter.Frame(window1)# armour section in bag page
    frame_bag_healingpad=tkinter.Frame(window1)# healing pad section in bag page
    frame_bag_key=tkinter.Frame(window1)# key section in bag page
    frame_bag_use=tkinter.Frame(window1)# wear gear in bag page
    frame_bag_takeoff=tkinter.Frame(window1)# take off gear button

   
    



    bag_back_to_menu_button=tkinter.Button(frame_bag_back_button,text="Back", command=page_switch5)
    bag_back_to_menu_button.grid(row=0,column=0)


    weapon_title=tkinter.Label(frame_bag_weapon, text="\n\n Weapons you have >>")
    weapon_title.grid(row=0,column=0)

    if len(player.bag[0])==0:
        weapon_show=tkinter.Label(frame_bag_weapon,text="You have no weapon yet.")
        weapon_show.grid(row=1,column=0)

    else:
        for w in range(len(player.bag[0])):

            weapon_show=tkinter.Label(frame_bag_weapon,text=player.bag[0][w].name+"        Damage: "+str(player.bag[0][w].damage)+"        Sale Price: "+str(player.bag[0][w].price*0.9))
            weapon_show.grid(row=w+1,column=0)

    armour_title=tkinter.Label(frame_bag_armour,text="\n\n Armours you have >>")
    armour_title.grid(row=0,column=0)

    if len(player.bag[1])==0:
        armour_show=tkinter.Label(frame_bag_armour,text="You have no armour yet.")
        armour_show.grid(row=1,column=0)

    else:
        for a in range (len(player.bag[1])):
            armour_show=tkinter.Label(frame_bag_armour,text=player.bag[1][a].name+"        Duability: "+str(player.bag[1][a].duability)+"        Sale Price: "+str(player.bag[1][a].price*0.9))
            armour_show.grid(row=a+1,column=0)

    healing_pad_title=tkinter.Label(frame_bag_healingpad,text='\n\n Healing pad >>')
    healing_pad_title.grid(row=0,column=0)

    if len(player.bag[2])==0:
        healingpad_show=tkinter.Label(frame_bag_healingpad,text="You don't have healing pads yet.")
        healingpad_show.grid(row=1,column=0)

    else:
        healingpad_show=tkinter.Label(frame_bag_healingpad,text=player.bag[2][0].name+'  *'+str(len(player.bag[2])))
        healingpad_show.grid(row=1,column=0)


    key_title=tkinter.Label(frame_bag_key,text='\n\n Key >>')
    key_title.grid(row=0,column=0)

    if len(player.bag[3])==0:
        key_show=tkinter.Label(frame_bag_key,text="You don't have keys yet.")
        key_show.grid(row=1,column=0)

    else:
        
        for g in range(len(player.bag[3])):

            key_show=tkinter.Label(frame_bag_key,text=player.bag[3][g].name+"        Code: "+str(player.bag[3][g].code))
            key_show.grid(row=1+g,column=0)

            

    
    wear_gear_gap=tkinter.Label(frame_bag_use,text="\n\n")
    wear_gear_gap.grid(row=0,column=0)

    wear_gear=tkinter.Entry(frame_bag_use)
    wear_gear.grid(row=1,column=0)

    wear_gear_button=tkinter.Button(frame_bag_use,text="Use",command=wearing_gear)
    wear_gear_button.grid(row=1,column=1)
   
    takeoff_gap=tkinter.Label(frame_bag_takeoff,text='\n')
    takeoff_gap.grid(row=0,column=0)


    takeoff_weapon_button=tkinter.Button(frame_bag_takeoff,text='Take off Weapon',command=takeoff_weapon)
    takeoff_weapon_button.grid(row=1,column=0)

    takeoff_armour_button=tkinter.Button(frame_bag_takeoff,text="Take off Armour",command=takeoff_armour)
    takeoff_armour_button.grid(row=1,column=1)
    

    


    frame_bag_back_button.pack()
    frame_bag_weapon.pack()
    frame_bag_armour.pack()
    frame_bag_healingpad.pack()
    frame_bag_key.pack()
    frame_bag_use.pack()
    frame_bag_takeoff.pack()
    
def room_pack(room,room_description,room_pic1,room_pic2):

    global frame_room_description,frame_room_buttons,treasurebox,open_box

    
    frame_room_description=tkinter.Frame(window1)
    frame_room_buttons=tkinter.Frame(window1)

   
    gap=tkinter.Label(frame_room_description,text='\n\n')
    gap.grid(row=0,column=0)

    if room.enermy['Health']==0:

        enermy_image=tkinter.Label(frame_room_description,image=room_pic2)
        enermy_image.grid(row=1,column=0)
        enermy_stat_=tkinter.Label(frame_room_description,text='Enermy status:  Defeated')
        enermy_stat_.grid(row=1,column=0)

        gap3=tkinter.Label(frame_room_buttons,text='\n\n')
        gap3.grid(row=0,column=0)
        

        if room.treasure['Exist']==True:
            treasurebox=tkinter.Label(frame_room_buttons, text='Treasure box')
            treasurebox.grid(row=1,column=0)
            open_box=tkinter.Button(frame_room_buttons,text='Open',command=lambda:open_treasure_box(room))
            open_box.grid(row=1,column=1)
            

        #if player.point_>=10:
            #page_switch_win()

        gap4=tkinter.Label(frame_room_buttons,text='\n')
        gap4.grid(row=2,column=0)

        leave_button=tkinter.Button(frame_room_buttons,text="Leave",command=page_switch7)
        leave_button.grid(row=3,column=1)

        

        



    else:

        
        enermy_image=tkinter.Label(frame_room_description,image=room_pic1)
        enermy_image.grid(row=1,column=0)

        enermy_stat_=tkinter.Label(frame_room_description,text='Enermy status:         '+room.enermy['Name']+'   Damage: '+str(room.enermy['Damage'])+'   Health: '+str(room.enermy['Health'])+'\n\n\n')
        enermy_stat_.grid(row=2,column=0)


        description=tkinter.Label(frame_room_description,text=room_description)
        description.grid(row=3,column=0)

    

       

        fight=tkinter.Button(frame_room_buttons,text='Fight!',command=lambda:page_switch8(room))
        fight.grid(row=3,column=0)
        leave=tkinter.Button(frame_room_buttons,text='Leave',command=page_switch7)
        leave.grid(row=3,column=1)
        

    frame_room_description.image=room_pic1,room_pic2
    frame_room_description.pack()
    frame_room_buttons.pack()


def room_fight(room):

    global frame_enermy_stat,frame_battle_field,line,line2,enermy_stat,frame_battle_button

    frame_enermy_stat=tkinter.Frame(window1)#show enermy status
    frame_battle_field=tkinter.Frame(window1)
    frame_battle_button=tkinter.Frame(window1)
    
    if room.enermy['Health']>0:

        gap=tkinter.Label(frame_enermy_stat,text='\n\n')
        gap.grid(row=0,column=0)
        enermy_stat=tkinter.Label(frame_enermy_stat,text='Enermy status:         '+room.enermy['Name']+'   Damage: '+str(room.enermy['Damage'])+'   Health: '+str(room.enermy['Health']))
        enermy_stat.grid(row=1,column=0)
        
        gap=tkinter.Label(frame_enermy_stat,text='\n\n')
        gap.grid(row=2,column=0)

        line=tkinter.Label(frame_battle_field,text='')
        line.grid(row=0,column=0)

        line2=tkinter.Label(frame_battle_field,text='')
        line2.grid(row=1,column=0)

        

        l=[0,1]
        choose=random.choice(l)
        if choose==0:
            room_player_attack(room)

        else:
            room_enermy_attack(room)

    
    
    

    frame_enermy_stat.pack()
    frame_battle_field.pack()
    frame_battle_button.pack()

def room_enermy_attack(room):


    enermy_lines=[room.enermy['Name']+' splited on your face!', room.enermy['Name']+' slapped you in the face!',room.enermy['Name']+' kicked your head!' ,room.enermy['Name']+' poisoned your Diet Coke!']
    choose_line=random.choice(enermy_lines)

    line.configure(text=choose_line)
    message=choose_line
    popup(message)
    
    if player.using['Armour']=='None':
        line2.configure(text='health -'+str(room.enermy['Damage'])+' !')

        if player.health_-room.enermy['Damage']>0:
            player.health_-=room.enermy['Damage']
            health.configure(text="Health: "+str(player.health_))

            for content in frame_battle_button.grid_slaves():
                content.grid_forget()
                content.destroy()

            gap=tkinter.Label(frame_battle_button,text='\n\n')
            gap.grid(row=0,column=0)
            button1=tkinter.Button(frame_battle_button,text='Run',command=page_switch9)
            button1.grid(row=1,column=0)
            button2=tkinter.Button(frame_battle_button,text='Fight Back',command=lambda:room_player_attack(room))
            button2.grid(row=1,column=1)
            

        else:
            player.health_=0
            health.configure(text="Health: "+str(player.health_))

            if player.point_>=2:
                player.point_-=2

                points.configure(text="Points: "+str(player.point_))
                for content in frame_battle_button.grid_slaves():
                    content.grid_forget()
                    content.destroy()

                lose_condition()


                                


                lose_message=tkinter.Label(frame_battle_button,text='You lose! Point -2')
                lose_message.grid(row=0,column=0)
                button=tkinter.Button(frame_battle_button,text='Leave',command=page_switch9)
                button.grid(row=1,column=0)
                

            else:

                page_switch_lose()
                
                

            


    else:
       

        if player.health_-room.enermy['Damage']/player.defense>0:
            line2.configure(text='health -'+str(room.enermy['Damage']/player.defense)+' !')
            player.health_-=room.enermy['Damage']/player.defense
            health.configure(text="Health: "+str(player.health_))

            for content in frame_battle_button.grid_slaves():
                content.grid_forget()
                content.destroy()

            gap=tkinter.Label(frame_battle_button,text='\n\n')
            gap.grid(row=0,column=0)
            button1=tkinter.Button(frame_battle_button,text='Run',command=page_switch9)
            button1.grid(row=1,column=0)
            button2=tkinter.Button(frame_battle_button,text='Fight Back',command=lambda:room_player_attack(room))
            button2.grid(row=1,column=1)

        else:
            player.health_=0
            health.configure(text="Health: "+str(player.health_))
            
            if player.point_>=2:
                player.point_-=2

                points.configure(text="Points: "+str(player.point_))
                for content in frame_battle_button.grid_slaves():
                    content.grid_forget()
                    content.destroy()

                lose_condition()

                lose_message=tkinter.Label(frame_battle_button,text='You lose! Point -2')
                lose_message.grid(row=0,column=0)
                button=tkinter.Button(frame_battle_button,text='Leave',command=page_switch9)
                button.grid(row=1,column=0)
                

            else:

                page_switch_lose()
            

   

def lose_condition():
    
    if player.using['Weapon']!='Fist' or player.using['Armour']!='None':
        message_lose='You lose! Point -2 and the enermy took all the shit you worn! '
        popup(message_lose)

        if player.using['Weapon']!='Fist':
            for item in player.bag[0]:
                if item.name==player.using['Weapon']:
                    player.using['Weapon']='Fist'
                    player.bag[0].remove(item)
                    #item.stock=1 #increase difficulty that user cannot buy the weapon back after losing it 
                    player.attack=3
                    configure_armed_gear_string()
                                
                    if item not in store.all_items:
                        store.weapon.append(item)
                        store.all_items.append(item)

        if player.using['Armour']!='None':
            for item in player.bag[1]:
                if item.name==player.using['Armour']:
                    player.using['Armour']='None'
                    player.bag[1].remove(item)
                    #item.stock=1
                    player.defense=0
                    configure_armed_gear_string()
                    if item not in store.all_items:
                        store.armour.append(item)
                        store.all_items.append(item)


    else:
        message_lose='You lose! Point -2'
        popup(message_lose)



def room_player_attack(room):

   
    if room.enermy['Health']-player.attack>0:

        line.configure(text='You attack with '+player.using['Weapon']+', enermy health -'+str(player.attack))
        room.enermy['Health']-=player.attack
        enermy_stat.configure(text='Enermy:         '+room.enermy['Name']+'   Damage: '+str(room.enermy['Damage'])+'   Health: '+str(room.enermy['Health']))

        line2.configure(text='')

        for content in frame_battle_button.grid_slaves():
            content.grid_forget()
            content.destroy()
        gap=tkinter.Label(frame_battle_button,text='\n\n')
        gap.grid(row=0,column=0)
        button1=tkinter.Button(frame_battle_button,text='Run',command=page_switch9)
        button1.grid(row=1,column=0)
        button2=tkinter.Button(frame_battle_button,text='Continue',command=lambda:room_enermy_attack(room))
        button2.grid(row=1,column=1)

        
    else:
        line.configure(text='You attack with '+player.using['Weapon']+', enermy health -'+str(player.attack))
        line2.configure(text='')
        room.enermy['Health']=0
        enermy_stat.configure(text='Enermy status:         '+room.enermy['Name']+'   Damage: '+str(room.enermy['Damage'])+'   Health: '+str(room.enermy['Health']))

        for content in frame_battle_button.grid_slaves():
            content.grid_forget()
            content.destroy()

        message='You win!!'
        popup(message)

        player.point_+=room.point
        points.configure(text="Points: "+str(player.point_))
        message_points='Point +'+str(room.point)
        popup(message_points)

        message_weapon='You won a '+room.weapons['Name']+', It has been added into your bag!'
        temp_weapon=weapon(room.weapons['Name'],room.weapons['Damage'],room.weapons['Price'],1)
        player.bag[0].append(temp_weapon)
        popup(message_weapon)


        player.money+=room.money
        money.configure(text="Money: "+str(player.money))
        message_money='You won $'+str(room.money)
        popup(message_money)

        if room.healing_pad_['Exist']==True:
            message_healing_pad='You collect a healing pad from the room, It has been added into your bag!'
            popup(message_healing_pad)
            player.bag[2].append(store.healing_pad[0])

        if room.keys['Exist']==True:
            message_keys='You collect a key from the room, It has been added into your bag!'
            popup(message_keys)
            temp_key=key(room.keys['Code'],room.keys['Price'])
            player.bag[3].append(temp_key)

        





        
        win_message=tkinter.Label(frame_battle_button,text='\n\nYou win!!')
        win_message.grid(row=0,column=0)
        button1=tkinter.Button(frame_battle_button,text='Continue',command=page_switch9)
        button1.grid(row=1,column=0)

        if player.point_>=10:
            page_switch_win()
        
    

   
def open_treasure_box(room):
    
    if len(player.bag[3])==0:
        message="You don't have a key. "
        popup(message)

    else:
        o=False
        for item in player.bag[3]:
            if item.code==room.treasure['Code']:
                o=True

                player.point_+=room.treasure['Point']
                points.configure(text="Points: "+str(player.point_))

                
                message2='Point +'+str(room.treasure['Point'])
                popup(message2)


                room.treasure['Exist']=False

                if player.point_>=10:
                    page_switch_win()

                treasurebox.destroy()
                open_box.destroy()

                



                break

        
        if o==False:
            message3="You don't have the key with correct code."
            popup(message3)






















def get_username():
    player.name=name_entrance.get()
   

def quit_game():
    window1.destroy()

def weapon_sort_damage():

    for i in range(len(store.weapon)):
        for j in range(len(store.weapon)-i-1):
            if store.weapon[j].damage < store.weapon[j+1].damage:
                temp=store.weapon[j+1]
                store.weapon[j+1]=store.weapon[j]
                store.weapon[j]=temp

    update_shop_weapon()

def weapon_sort_price():

    for i in range(len(store.weapon)):
        for j in range(len(store.weapon)-i-1):
            if store.weapon[j].price > store.weapon[j+1].price:
                temp=store.weapon[j+1]
                store.weapon[j+1]=store.weapon[j]
                store.weapon[j]=temp

    update_shop_weapon()

def update_shop_weapon():

    

    for texts in frame_shop_weapon.grid_slaves():# access all elements under grid of frame_shop_weapon
        texts.grid_forget()# hide content
        texts.destroy() # destroy from memory to prevent bug when switch too many times

    

    for i in range(len(store.weapon)): #rewrite 
        shop_weapon1=tkinter.Label(frame_shop_weapon, text=store.weapon[i].name +"         Damage: "+str(store.weapon[i].damage)+"         Price: "+str(store.weapon[i].price)+"         Stock:"+str(store.weapon[i].stock))
        shop_weapon1.grid(row=i,column=0)


def armour_sort_duability():

    for i in range(len(store.armour)):
        for j in range(len(store.armour)-i-1):
            if store.armour[j].duability < store.armour[j+1].duability:
                temp=store.armour[j+1]
                store.armour[j+1]=store.armour[j]
                store.armour[j]=temp

    update_shop_armour()   

def armour_sort_price():

    for i in range(len(store.armour)):
        for j in range(len(store.armour)-i-1):
            if store.armour[j].price > store.armour[j+1].price:
                temp=store.armour[j+1]
                store.armour[j+1]=store.armour[j]
                store.armour[j]=temp

    update_shop_armour()   


def update_shop_armour():

    for texts in frame_shop_armour.grid_slaves():
        texts.grid_forget()
        texts.destroy()

    shop_category=tkinter.Label(frame_shop_armour,text="\n \n Armours:                                                                      ")
    shop_category.grid(row=0,column=0)

    for i in range(len(store.armour)):
        shop_armour1=tkinter.Label(frame_shop_armour, text=store.armour[i].name +"         Duability: "+str(store.armour[i].duability)+"         Price: "+str(store.armour[i].price)+"         Stock:"+str(store.armour[i].stock))
        shop_armour1.grid(row=i+1,column=0)

def update_shop_healing_pad():

    

    for texts in frame_shop_healing_pad.grid_slaves():
        texts.grid_forget()
        texts.destroy()
        

        
    shop_category_healing_pad=tkinter.Label(frame_shop_healing_pad,text="\n\n "+str(store.healing_pad[0].name)+"        Health Increase: "+str(store.healing_pad[0].power)+"       Price: "+str(store.healing_pad[0].price)+"        Stock: "+str(store.healing_pad[0].stock))
    shop_category_healing_pad.grid(row=0,column=0)


def update_shop_key():

    for texts in frame_shop_key.grid_slaves():
        texts.grid_forget()
        texts.destroy()

    for i in range (len(store.key)):
        shop_category_key=tkinter.Label(frame_shop_key,text="\n\n" + store.key[i].name + "        Code: "+str(store.key[i].code)+"        Price: "+str(store.key[i].price)+"        Stock: " + str(store.key[i].stock))
        shop_category_key.grid(row=i,column=0)
    



def purchasing():

    item=buy_entrance.get()

    if item=='':
        message="What???"
        popup(message)



    find=False

    for things in store.all_items:

            
            if things.name==item:

                find=True
                    
                if things.stock>0 and player.money>=things.price:
                    
                    player.money-=things.price
                    things.stock-=1
                    

                    money.configure(text='Money: '+str(player.money))
                    message='Cheers mate.'
                    popup(message)

                    if things in store.weapon:
                        player.bag[0].append(things)
                        
                        update_shop_weapon()

                    elif things in store.armour:
                        player.bag[1].append(things)
                        update_shop_armour()


                    elif things in store.healing_pad:
                        
                        update_shop_healing_pad()
                        player.bag[2].append(things)

                    elif things in store.key:

                        player.bag[3].append(things)
                        update_shop_key()
                        
                    break

                    
                        

                elif things.stock<1 and player.money<things.price:
                    message='Item is out of stock. Beside, go get some money first you broke ass prick.'
                    popup(message)
                    break

                elif things.stock<1:
                    message='Sorry mate, we are currently out of stock right now.'
                    popup(message)
                    break

                elif player.money<things.price:
                    message='Get some money first mate fok off'
                    popup(message)
                    break
        
            

    
    if find==False and item!='':
        message='We dont have that, are you playing with me you cheeky bastard? '
        popup(message)



def selling():
    item_name=sell_entrance.get()

    if item_name=='':
        message='What??'
        popup(message)
    
    else:
        if item_name not in player.using['Weapon'] and item_name not in player.using['Armour']:
            
            find=False
            
            for thing in player.bag[0]:
                if thing.name==item_name:
                    find=True
                    message2='Cheers mate!'
                    popup(message2)

                    player.bag[0].remove(thing)
                    player.money+=0.9*thing.price
                    money.configure(text='Money: '+str(player.money))


                    if thing in store.weapon:
                        thing.stock+=1
                        update_shop_weapon()
                        
                        break
                    
                    else:
                        store.weapon.append(thing)
                        store.all_items.append(thing)
                        update_shop_weapon()
                        
                        break

                

            for thing2 in player.bag[1]:
                if thing2.name==item_name:
                    find=True
                    message_sell_armour='Cheers mate!'
                    popup(message_sell_armour)

                    player.bag[1].remove(thing2)
                    player.money+=thing2.price*0.9
                    money.configure(text='Money: '+str(player.money))

                    if thing2 in store.armour:
                        thing2.stock+=1
                        update_shop_armour()
                        break

                    else:
                        store.armour.append(thing2)
                        store.all_items.append(thing2)
                        update_shop_armour()
                        break

               

            
            
            
            if find==False:
                
                find2=False

                for thing3 in player.bag[2]:
                    if thing3.name==item_name:
                        find2=True
                        message3='We do not buy this bro.'
                        popup(message3)
                        break

                    
                
                
                for thing4 in player.bag[3]:

                    if thing4.name==item_name:
                        find2=True
                        popup(message3)
                        break

                    

        
                if find2==False:
                    message4='You do not have this shit bro are you foking kidding me?'
                    popup(message4)


        
           
                    
        
        else:
            message5='You have to take it off first!'
            popup(message5)



def popup(message):

    messagebox.showinfo(message=message)


def wearing_gear():



    gear_to_wear= wear_gear.get()
    if gear_to_wear=="":
        message_Empty_input="What??"
        popup(message_Empty_input)
    
    else:

        if gear_to_wear in player.using['Weapon'] or gear_to_wear in player.using['Armour']:
            message_already_wearing='You already wearing it!'
            popup(message_already_wearing)

        else:

                find=False

                for items in player.bag[0]:

                    if items.name==gear_to_wear:
                        find=True
                        player.attack=3+items.damage
                        player.using['Weapon']=items.name
                        messageOK="Done!"
                        popup(messageOK)
                        break

                    


                for items in player.bag[1]:
                    if items.name==gear_to_wear:
                        find=True
                        player.defense=items.duability
                        player.using['Armour']=items.name
                        messageOK="Done!"
                        popup(messageOK)
                        break

                for items in player.bag[2]:
                    if items.name==gear_to_wear:
                        find=True
                        if player.health_==100:
                            message_max_health='You cannot use this because your health is currently 100!'
                            popup(message_max_health)

                        else:
                            if player.health_+items.power>=100:
                                player.health_=100

                            else:
                                player.health_+=items.power

                            messageOK="Done!"
                            popup(messageOK)
                            health.configure(text="Health: "+str(player.health_))
                            player.bag[2].remove(player.bag[2][-1])

                            for content in frame_bag_healingpad.grid_slaves():
                                content.grid_forget()
                                content.destroy()

                            healing_pad_title=tkinter.Label(frame_bag_healingpad,text='\n\n Healing pad >>')
                            healing_pad_title.grid(row=0,column=0)

                            if len(player.bag[2])==0:
                                healingpad_show=tkinter.Label(frame_bag_healingpad,text="You don't have healing pads yet.")
                                healingpad_show.grid(row=1,column=0)

                            else:
                                healingpad_show=tkinter.Label(frame_bag_healingpad,text=player.bag[2][0].name+'  *'+str(len(player.bag[2])))
                                healingpad_show.grid(row=1,column=0)

                            

                        break

                    

                    
                if find==False:

                    find2=False

                    for item in player.bag[3]:

                        if item.name==gear_to_wear:
                            find2=True
                            message="You cannot use a key without treasure box mate."
                            popup(message)
                            break

                    

                    if find2==False:
                            message="You don't have it."
                            popup(message)


                configure_armed_gear_string()

def takeoff_armour():
    
    if player.using['Armour']=='None':
        message="You ain't wearing shit bro"
        popup(message)

    else:
        player.using['Armour']='None'
        player.defense=0
        message='Done!'
        popup(message)

    configure_armed_gear_string()


def takeoff_weapon():

    if player.using['Weapon']=='Fist':
        message="You ain't using any weapon bro are you dumb?"
        popup(message)

    else:
        player.using['Weapon']='Fist'
        player.attack=3
        message='Done!'
        popup(message)

    configure_armed_gear_string()



def page_swtich1(): # after user enter username (submit button of entering username)
    get_username()
    frame_prompt_username.destroy()
    information_frame_pack()
    menu_frame_pack()

def page_switch2(): # shop button in menu
    
    frame_buttons.destroy()
    shop_frame_pack()

def page_switch3(): # back button in shop page
    
    frame_shop_back_button.destroy()
    frame_shop.destroy()
    frame_shop_weapon.destroy()
    frame_shop_sort.destroy()
    frame_shop_armour.destroy()
    frame_shop_sort_armour.destroy()
    frame_shop_healing_pad.destroy()
    frame_shop_buy.destroy()
    frame_shop_key.destroy()
    frame_shop_sell.destroy()

    menu_frame_pack()

def page_switch4(): # bag button in menu

    frame_buttons.destroy()
    bag_frame_pack()

def page_switch5(): # back button in bag page
    frame_bag_back_button.destroy()
    frame_bag_weapon.destroy()
    frame_bag_armour.destroy()
    frame_bag_healingpad.destroy()
    frame_bag_key.destroy()
    frame_bag_use.destroy()
    frame_bag_takeoff.destroy()
    
    
    menu_frame_pack()

def page_switch6(): # room1 button in menu
    frame_buttons.destroy()
    room1_des_=open('Room1.txt','r')
    room1_des=room1_des_.read()
    room1_des_.close() 

    qyburn_image1_=Image.open('qyburn1.png')
    qyburn_image1=ImageTk.PhotoImage(qyburn_image1_)

    qyburn_image2_=Image.open('qyburn2.png')
    qyburn_image2=ImageTk.PhotoImage(qyburn_image2_)


    room_pack(room1,room1_des,qyburn_image1,qyburn_image2)

def page_switch7(): # leave button in room info page

    frame_room_description.destroy()
    frame_room_buttons.destroy()
    menu_frame_pack()

def page_switch8(room): # fight button in room info page

    frame_room_description.destroy()
    frame_room_buttons.destroy()
    room_fight(room)

def page_switch9(): # run button during fighting

    frame_enermy_stat.destroy()
    frame_battle_field.destroy()
    frame_battle_button.destroy()
    menu_frame_pack()

def page_switch10(): # room2 button in menu

    frame_buttons.destroy()
    room2_des_=open('Room2.txt','r')
    room2_des=room2_des_.read()
    room2_des_.close() 

    snow_image1_=Image.open('johnsnow1.png')
    snow_image1=ImageTk.PhotoImage(snow_image1_)

    snow_image2_=Image.open('johnsnow2.png')
    snow_image2=ImageTk.PhotoImage(snow_image2_)


    room_pack(room2,room2_des,snow_image1,snow_image2)

def page__switch11(): # room3 button in menu

    frame_buttons.destroy()
    room3_des_=open('Room3.txt','r')
    room3_des=room3_des_.read()
    room3_des_.close()

    rob_image1_=Image.open('robstark1.png')
    rob_image1=ImageTk.PhotoImage(rob_image1_)

    rob_image2_=Image.open('robstark2.png')
    rob_image2=ImageTk.PhotoImage(rob_image2_)

    room_pack(room3,room3_des,rob_image1,rob_image2)

def page_switch12(): # room4 button in menu 

    frame_buttons.destroy()
    room4_des_=open('Room4.txt','r')
    room4_des=room4_des_.read()
    room4_des_.close()

    drogo_image1_=Image.open('drogo1.png')
    drogo_image1=ImageTk.PhotoImage(drogo_image1_)

    drogo_image2_=Image.open('drogo2.png')
    drogo_image2=ImageTk.PhotoImage(drogo_image2_)

    room_pack(room4,room4_des,drogo_image1,drogo_image2)










def page_switch_lose(): # player loses the game

    frame_enermy_stat.destroy()
    frame_battle_field.destroy()
    frame_battle_button.destroy()
    frame_informations.destroy()

    frame_lose=tkinter.Frame(window1)

    lose_image_=Image.open('lose.jpg')
    lose_image=ImageTk.PhotoImage(lose_image_)

    lose_graph=tkinter.Label(frame_lose,image=lose_image)
    lose_graph.grid(row=0,column=0)

    button1=tkinter.Button(frame_lose,text='Quit the game',command=quit_game)
    button1.grid(row=1,column=0)

    frame_lose.pack(expand=True)
    frame_lose.image = lose_image
            
def page_switch_win(): # player wins the game

    frame_enermy_stat.destroy()
    frame_battle_field.destroy()
    frame_battle_button.destroy()
    frame_informations.destroy()
    frame_room_description.destroy()
    frame_room_buttons.destroy()

    frame_win=tkinter.Frame(window1)

    win_image_=Image.open('win.jpg')
    win_image=ImageTk.PhotoImage(win_image_)
    win_graph=tkinter.Label(frame_win, image=win_image)
    win_graph.grid(row=0,column=0)
    button1=tkinter.Button(frame_win,text='Quit the game',command=quit_game)
    button1.grid(row=1,column=0)

    frame_win.pack(expand=True)
    frame_win.image=win_image





room1_info_=open('Room1.txt','r')
room1_info=room1_info_.readlines()
room1_info_.close()
room1=extract_information_rooms(room1_info)

room2_info_=open('Room2.txt','r')
room2_info=room2_info_.readlines()
room2_info_.close()
room2=extract_information_rooms(room2_info)


room3_info_=open('Room3.txt','r')
room3_info=room3_info_.readlines()
room3_info_.close()
room3=extract_information_rooms(room3_info)

room4_info_=open('Room4.txt','r')
room4_info=room4_info_.readlines()
room4_info_.close()
room4=extract_information_rooms(room4_info)


player=User()
store=shop()
extract_and_implement_items_shop()





window1 = tkinter.Tk()
window1.title("Python assessment 3")
window1.geometry('1200x1200')
first_page_frames_pack()


window1.mainloop()