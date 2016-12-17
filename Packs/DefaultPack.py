database = {
    "House":{
         "description":"It's an old house, it's a little drafty...it could be haunted",
         "objects_in_building" : ["a lantern","pickaxe"],
         "directions":("Blacksmiths","Business","Pond","Supermarket"),
         "type":"Home_point"},
    "Friends House" :{
                 "description":"Its a modern house full of electronics and computers",
                 "objects_in_building":["your friend","your friend's computer","a large fridge"],
                 "directions":("House","Village Hall","Cave"),
                 "type":"Sleeping_point"},
    "Pond":{
        "description":"Its a nice big pond, great for fishing and making wishes!",
        "objects_in_building":["a fish","coin toss stall"],
        "directions":("Friends House","Blacksmiths","House"),
        "type":"General_point"},
    "Village Hall":{
                "description":"A nice medieval hall, full of boxes, mabye there is something in them",
                "objects_in_building":["nothing","a crate"],
                "directions":("Blacksmiths","Friends House","Cave"),
                "type":"General_point"},
    "Blacksmiths":{
               "location_name" : "Blacksmiths",
               "description": "You are in an old and deserted building, you hear a slight creaking of rusting iron",
               "objects_in_building" : ["an elderly blacksmith"],
               "directions" : ('Village Hall','Pond','House',"Supermarket"),
               "type":"Buying_point"},
    "Business":{"location_name":"business",
            "description":"unlike the rest of the village they will employ you",
            "objects_in_building":["a front desk","three workers"],
            "directions":["House","Forest"],
            "type":"Work_point"},
    "Supermarket":{"location_name":"Super Market",
                "description":"you can buy your food here, there is a pineapple in the frozen foods isle.",
                "objects_in_building":["a ticket","a pineapple","a carrot","a raw chicken","a frozen yogurt","a z-box game","a rotten fish"],
                "directions":["Blacksmiths","House"],
                "type":"Selling_point"},
    "Cave":{"location_name":"Cave",
            "description":"very cold and quite dusty, you need a lantern to move here.",
            "objects_in_building":["gold","dust","spider"],
            "directions":("Village Hall","Friends House"),
            "dependency":"a lantern",
            "type":"Mining_point"},
    "Forest":{"location_name":"Forest",
              "description":"A haunted forest, you will need a lantern to move here.",
              "objects_in_building":[],
              "directions":("Business","Friends House"),
              "dependency":"a lantern",
              "type":"General_point"},
    "Portal":{"location_name":"Portal",
              "description":"Somewhere for other players to drop in",
              "objects_in_building":[],
              "directions":["House","Friends House","Pond","Village Hall","Blacksmiths"],
              "type":"General_point"},
    }

object_database = {
    "a leaf":{
        "attack" : 2,
        "description" : "a clear leaf from a diamond tree",
        "type":"attack"},
    "fingers":{
        "attack" : 1,
        "description" : "a bright lantern, made of steel and gold",
        "type":"attack"},
    "spear":{
        "attack" : 3,
        "description" : "It's a short plastic spear, not the most fierce weapon I've seen.",
        "type":"attack"},
    "a lantern":{
        "description":"casts a bright light around the room",
        "type":"general"},
    "a carrot":{
        "attack":0,
        "description":"a tastey treat, and its very nutritious!",
        "type":"eat"},
    "your freind":{
        "attack":2,
        "description":"your loyal best friend!!!",
        "type":"attack"},
    "your friend's computer":{
        "attack":0,
        "description":"a really fast computer with 9999999TetraBytes of RAM and CPU",
        "type":"general"},
    "a large fridge":{
        "attack":0,
        "description":"a gleaming white fridge filled with choclate, cake and chocolate cake",
        "type":"general"},
    "a fish":{
        "attack":0,
        "description":"you can buy lots of nice cuts of fish from here, only 6 weeks off!!!",
        "type":"general"},
    "coin toss stall":{
        "attack":0,
        "description":"you can waste a coin here is you wish",
        "type":"general"},
    "an elderly blacksmith":{
        "attack":5,
        "description":"if you are holding him he will fight for you!",
        "type":"attack"},
    "a front desk":{
        "attack":0,
        "description":"a nice oak desk from IKEA",
        "type":"general"},
    "three workers":{
        "attack":6,
        "description":"will fight for you with their pens and three ring binders",
        "type":"attack"},
    "a pineapple":{
        "attack":0,
        "description":"its a pineapple, end of story",
        "type":"eat"},
    "a raw chicken":{
        "attack":0,
        "description":"yum! yum! NOT, eat this at your own risk",
        "type":"eat"},
    "a frozen yogurt":{
        "attack":0,
        "description":"It hurts your teeth doesn't it? try to defrost it first",
        "type":"eat"},
    "a z-box game":{
        "attack":0,
        "description":"A very fun game to play, unforchunately you don't hav a z-box to play it on",
        "type":"general"},
    "a rotten fish":{
        "attack":0,
        "description":"YUK, a rotten fish, why are you even looking at this?",
        "type":"eat"},
    "gold":{
        "attack":0,
        "description":"a really rare resource, oh and it wins the game",
        "type":"general"},
    "dust":{
        "attack":0,
        "description":"don't even think of picking this up!, it has no use DON'T EVEN THINK ABOUUT IT!",
        "type":"general"},
    "spider":{
        "attack":2,
        "description":"a really tiny spider, it will fight for you against monsters though",
        "type":"attack"},
    "nothing":{
        "attack":99999,
        "description":"can kill Death itself",
        "type":"attack"},
    "pickaxe":{
        "attack":2,
        "description":"Use this pickaxe to mine iron to make swords and armour",
        "type":"gerneral"},
    "Steel Sword":{
        "attack":4,
        "description":"a basic sword made out of 2 iron",
        "type":"attack"},
    "squashed monster in a bottle":{
        "attack":0,
        "description":"if you put it in your house, you can have a bonus of health each round",
        "type":"magical"},
    "broken sword":{
        "attack":0,
        "description":"if you put it in your house, you can have a bonus of health each round",
        "type":"magical"},
    }



monster_database = {
   "hairy spider":{
        "name":"Incy wincy spider",
        "description":"very large and hairy, has lots of poison",
        "health":5,
        "picture":":)"},
   "small spider":{
        "name":"Incy wincy spider",
        "description":"Tiny spider, not very harmful, but people scream anyway.",
        "health":4,
        "picture":":)"},
   "really massive miniscule destuctive peaceful undead rabbit":{
       "name":"Really Massive Miniscule Destuctive Peaceful Undead Rabbit",
       "description":"terrorizes the other towns and citys with its pointy nose",
       "health":7,
       "picture":":)"},
   "Death":{
       "name":"Death",
       "description":"kills you instantly",
       "health":99998,
       "picture":":)"},
   "unspecial monster":{
       "name":"unspecial monster",
       "description":"has no special powers,he uses his face",
       "health":7,
       "picture":":)"},
   "the inediable bulk":{
       "name":"the inediable bulk",
       "description":"supprisingly you cannot eat it!,run if you have pizza and chips",
       "health":10,
       "picture":":)"},
   }

