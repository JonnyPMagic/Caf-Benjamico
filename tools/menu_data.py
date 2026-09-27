# Speisekarte – Quelle für speisekarte.html (Build: python3 tools/build_speisekarte.py)
# Kennzeichnung: veg = vegetarisch, vegan = vegan, new = Neu

FRUEHSTUECK = [
    dict(name="Vegetarisches Frühstück", price="12,90", tag="veg", allergens="A,G,L",
         desc="1 Brötchen, Sauerteigbrot, Butter, Honig Chili Butter, Erdbeerkonfitüre, Emmentaler, Frischkäse, hausgemachter Linsenaufstrich, Joghurt mit hausgemachtem Granola und saisonales Obst"),
    dict(name="Herzhaftes Frühstück", price="12,90", allergens="A,G,J",
         desc="1 Brötchen, Sauerteigbrot, Butter, Honig Chili Butter, Erdbeerkonfitüre, Emmentaler, Brie, Schwarzwälder Schinken, Grillgemüse, saisonales Obst, Feigensenf"),
    dict(name="Veganes Frühstück", price="12,90", tag="vegan", allergens="A,F,K,L",
         desc="1 Brötchen, Sauerteigbrot, vegane Butter, Erdbeerkonfitüre, veganer Joghurt mit hausgemachtem Granola, hausgemachter Linsenaufstrich, Grillgemüse, Avocado, Ofenkürbis & saisonales Obst"),
    dict(name="Rührei", price="4,50", tag="veg", allergens="C", desc="von 3 Bio-Eiern mit Schnittlauch"),
    dict(name="Bergmanns Frühstück", price="9,50", allergens="A,G,J,I",
         desc="Sauerteigbrot, Butter, Lyoner, Senf, Bruch Saarbrücker Hell oder Limonade"),
    dict(name="Vegan Scrambled Tofu", price="4,50", tag="vegan", allergens="F", desc="Vegane Rührei-Alternative"),
    dict(name="Eier Benedikt", price="10,90", tag="veg", allergens="A,C,G,I,L",
         desc="Eine Scheibe getoastetes Sauerteigbrot, 2 pochierte Eier, Sauce Hollandaise, Wildkräutersalat"),
]

EXTRAS = [
    ("Hausgebeizter Lachs", "D,L", "5,50"),
    ("Griechischer Joghurt (G) oder veganer Joghurt (F) mit hausgemachtem Granola (A,H) und saisonalen Früchten – auf Wunsch mit Honig oder Ahornsirup", "", "4,90"),
    ("Brotkorb (1 Scheibe Sauerteigbrot, 1 Brötchen)", "A", "2,90"),
    ("Bagel", "A,K", "2,40"),
    ("Butter oder Honig Chili Butter", "G", "1,50"),
    ("Bacon", "", "2,50"),
    ("Linsenaufstrich", "L", "1,80"),
    ("Avocado", "", "2,90"),
    ("Erdbeerkonfitüre", "", "1,50"),
    ("Croissant", "A,C,G", "2,60"),
]

BAGELS = [
    dict(name="Lachs Avocado Bagel", price="10,50", allergens="A,D,G,K,L",
         desc="Bagel (Brot & Sinne) mit Frischkäse, hausgebeiztem Lachs, Avocado, eingelegten Zwiebeln, Wildkräutersalat"),
    dict(name="Burrata Tomate Stulle", price="12,80", allergens="A,G,L",
         desc="1 Scheibe Sauerteigbrot (Brot & Sinne), Burrata, hausgemachtes grünes Pesto, geschmorte Tomaten, Rucola"),
    dict(name="Good Morning Vegan", price="8,50", tag="vegan", allergens="A,K,L",
         desc="Bagel (Brot & Sinne) mit hausgemachtem Linsenaufstrich, Grillgemüse, Granatapfelkernen, Rucola & Sprossen"),
    dict(name="Strammer Max", price="9,50", allergens="A,C,G,L",
         desc="1 Scheibe Sauerteigbrot (Brot & Sinne), Butter, Wildkräutersalat, Spiegelei, Gewürzgurken, Schwarzwälder Schinken, Emmentaler",
         extra=["Große Portion mit 2 Scheiben Brot +3,50"]),
    dict(name="Avocado Tomate Stulle", price="11,80", tag="vegan", allergens="A,L",
         desc="1 Scheibe Sauerteigbrot (Brot & Sinne), Avocado, Piment d’Espelette, geschmorte Tomaten, Rucola"),
]

SWEET = [
    dict(name="French Toast Whiskey Ahorn Bacon", price="11,50", allergens="A,C,G", signature=True,
         desc="2 Scheiben Brioche, Mascarpone-Vanillecreme, Whisky-Ahornsirup, Bacon, Schnittlauch"),
    dict(name="French Toast Waldbeere", price="10,50", tag="veg", allergens="A,C,G",
         desc="2 Scheiben Brioche, Mascarpone-Vanillecreme, hausgemachtes Beerenkompott mit Zimt, Ahornsirup, Puderzucker"),
    dict(name="French Toast Lotus Cheesecake", price="11,90", tag="veg", allergens="A,C,G,F",
         desc="2 Scheiben Brioche mit Mascarpone-Lotus-Creme, Lotus Crumble & Karamellsauce"),
    dict(name="Sweet Stuffed Croissant Zimt & Beere", price="8,00", tag="veg", allergens="A,C,G",
         desc="Croissant gefüllt mit Erdbeerkonfitüre, Mascarpone-Vanillecreme, hausgemachtem Beerenkompott mit Zimt"),
]

LUNCH = [
    dict(name="Herbst Bowl", price="12,90", tag="veg", new=True, allergens="A,I,J,L",
         desc="Couscous, Avocado, Gurke, Kichererbsen, Ofenkürbis, Rucola, Feta, Granatapfelkerne",
         extra=["Toppings: hausgebeizter Lachs +5,50 (D,L)", "Tofu +3,50 (F)", "pochiertes Ei +2,50 (C,L)"]),
    dict(name="Pastrami Melt Sandwich", price="13,90", new=True, allergens="A,C,G,I,J,L",
         desc="2 Scheiben gegrilltes Bergbrot (Brot & Sinne) mit New York Pastrami, Cheddar, Honig-Dijon-Creme, Sandwichgurken, eingelegten roten Zwiebeln, Rucola"),
    dict(name="Kürbis-Salbei-Pasta", price="12,50", tag="veg", new=True, allergens="A,G,I,L",
         desc="Pasta in cremiger Kürbis-Salbei-Sauce, Ofenkürbis, Parmesan",
         extra=["+ Burrata 5,50", "+ pochiertes Ei 2,50", "+ Tofu 3,50"]),
    dict(name="Currywurst – klassisch oder vegan", price="6,50", tag="vegan-option", allergens="klassisch A,I,L,J · vegan A,F,I,L,J",
         desc="Hausgemachte Currysauce mit frischem Sauerteigbrot (Brot & Sinne) oder Brötchen, dazu ein kleiner Salat"),
    dict(name="Herbsteintopf", price="9,90", tag="vegan", new=True, allergens="A,F,I,K,L",
         desc="Herzhafter Eintopf mit Kartoffeln, Karotten, Lauch, weißen Bohnen und Kräutern, dazu geröstetes Bergbrot von Brot & Sinne"),
]

MILCH = "Sie haben die Wahl zwischen Kuhmilch (G), Haferdrink (A) oder Sojadrink (F)."

GETRAENKE = [
    ("Kaffee", [
        ("Americano", "", "2,90"), ("Cappuccino", "", "3,60"), ("Milchkaffee", "", "3,80"),
        ("Latte Macchiato", "", "4,20"), ("Flat White", "", "4,00"), ("Espresso", "", "2,20"),
        ("Espresso Doppio", "", "3,40"),
    ], MILCH),
    ("Heißgetränke", [
        ("Matcha Latte", "", "4,80"), ("Ube Latte", "", "5,50"), ("Dirty Ube Latte", "new", "6,20"),
        ("Chai Latte", "new", "5,20"), ("Dirty Chai Latte", "new", "5,90"), ("Pumpkin Cloud Latte", "new", "5,90"),
        ("Heiße Schokolade", "", "3,60"), ("Althaus Trink Meer Tee", "verschiedene Sorten im Beutel", "3,50"),
        ("Babyccino", "aufgeschäumte Milch", "1,00"),
    ], None),
    ("Iced Drinks", [
        ("Iced Latte Macchiato", "", "4,20"), ("Iced Matcha Latte", "", "4,80"),
        ("Iced Strawberry Matcha Latte", "", "5,60"), ("Iced Ube Latte", "", "5,50"),
        ("Iced Dirty Ube Latte", "new", "6,20"), ("Iced Chai Latte", "new", "5,20"),
        ("Iced Dirty Chai Latte", "new", "5,90"), ("Iced Pumpkin Cloud Latte", "new", "5,90"),
        ("Kokos-Drachenfrucht Refresher", "", "5,90"),
        ("Caramel Cloud Latte", "Iced Latte mit Karamellsirup, Cream Top (G) und Biscoff Crumble (A,G,F)", "5,60"),
        ("+ Sirup Ihrer Wahl", "", "0,50"),
    ], MILCH),
    ("Kaltgetränke", [
        ("Wasser 0,25 / 0,75 l", "Gerolsteiner still / sprudelnd", "2,40 / 4,80"),
        ("Säfte 0,2 l", "Apfel, Traube, Orange, Grapefruit", "3,10"),
        ("Saftschorle 0,3 l", "", "3,50"), ("Afri Cola / Zero", "", "3,60"),
        ("Bluna Orange / Zitrone", "", "3,50"), ("Bruch Kalter Kaffee", "Cola-Orange-Mix", "3,60"),
        ("Coldleaf Eistee", "Pfirsich oder Drachenfrucht", "3,90"),
    ], None),
    ("Bier", [
        ("Bruch Saarbrücker Hell", "", "3,60"), ("Bruch Pilsener alkoholfrei", "", "3,60"),
        ("Maisel’s Hefeweizen (A)", "", "4,90"), ("Maisel’s Weizen alkoholfrei (A)", "", "4,90"),
    ], None),
    ("Wein & Sekt", [
        ("Manz Riesling 0,2 / 0,75 l (L)", "Rheinhessen Kalkstein, feinherb", "7,90 / 29,50"),
        ("Manz Grauburgunder 0,2 / 0,75 l (L)", "Rheinhessen, trocken", "7,60 / 28,00"),
        ("Weinschorle 0,2 l (L)", "", "5,20"),
        ("Crémant de Loire 0,1 / 0,75 l (L)", "", "5,80 / 28,00"),
    ], None),
]

SPECIALS = [
    ("Aperol Spritz (L)", "", "7,90", False),
    ("Espresso Martini (L)", "Wodka, Kaffeelikör, Espresso, Zuckersirup", "8,50", True),
    ("Grapefruit Rosemary Fizz (alkoholfrei)", "Grapefruitsaft, Zitronensaft, Rosmarinsirup", "7,00", False),
]

ALLERGENE = [("A", "Gluten"), ("B", "Krebstiere"), ("C", "Eier"), ("D", "Fisch"), ("E", "Erdnüsse"),
             ("F", "Soja"), ("G", "Milch"), ("H", "Schalenfrüchte (Nüsse)"), ("I", "Sellerie"), ("J", "Senf"),
             ("K", "Sesam"), ("L", "Sulfite"), ("M", "Lupine"), ("N", "Weichtiere")]
