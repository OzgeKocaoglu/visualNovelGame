# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Can = Character("Can")
define Ergun = Character("Ergun")
define Melih = Character("Melih")
define Yesim = Character("Yeşim")
define Ozge = Character("Özge")


# The game starts here.

label start:
    scene bg 01
    with fade
    "Beş arkadaş League of Legens oynamaktadır."
    "Sıradan bir dereceli maçıdır."

label sprites:
    show can
    with dissolve
    Can "Abi Kayn sıkıntı abi ya."
    show ergun at right
    with dissolve
    Ergun "Teemo almış it oğlu it"
    show melih at left
    Melih "Yeşim sakin oyna, ben yardıma gelicem"
    hide can
    hide melih
    hide ergun
    show yesim at right
    Yesim "Tamam"
    "Oyun sakin bir şekilde başlar. Can kırmızıdan başlayarak üst ormana girer."
    Can "Kayn geliyo! Geliyo! Ormanıma giriyo!"
    Can "Yeşim Yeşim! Blue'ya gel."
    Yesim "Blue ne taraftı?"
    Can "ÖLDÜM YA!"
    "İlk kan döküldü"
    "Bir rakip katledildi."
    Ergun "Teemo alan bu itleri böyle cezalandırmak lazım."
    "Bu sırada bot lane'de dengeler değişmektedir."
    Ozge "Birazdan giriyoruz."
    Ozge "Bu kim ya? Almış Jhin bu kim? Gel buraya. Kim bu kim-"
    "Takım arkadaşlarından birisi katledildi."

label background:

    return
