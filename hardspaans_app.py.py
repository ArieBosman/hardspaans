import random

# HARD-werkwoorden (20 stuks)
verbs = [
    "venir", "decir", "hacer", "poner", "ver", "ir", "ser",
    "escribir", "abrir", "leer", "oír", "construir",
    "elegir", "seguir", "recordar", "volver", "romper",
    "traer", "conducir", "dormir"
]

persons = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]
tenses = ["presente", "perfecto", "imperfecto", "gerundio"]

# Presente onregelmatigheden
def present_irregular(verb, person):
    # venir
    if verb == "venir":
        forms = {
            "yo": "vengo", "tú": "vienes", "él/ella": "viene",
            "nosotros": "venimos", "vosotros": "venís", "ellos": "vienen"
        }
        return f"{person} {forms[person]}"

    # decir
    if verb == "decir":
        forms = {
            "yo": "digo", "tú": "dices", "él/ella": "dice",
            "nosotros": "decimos", "vosotros": "decís", "ellos": "dicen"
        }
        return f"{person} {forms[person]}"

    # hacer
    if verb == "hacer" and person == "yo":
        return "yo hago"

    # poner
    if verb == "poner" and person == "yo":
        return "yo pongo"

    # ver
    if verb == "ver":
        forms = {
            "yo": "veo", "tú": "ves", "él/ella": "ve",
            "nosotros": "vemos", "vosotros": "veis", "ellos": "ven"
        }
        return f"{person} {forms[person]}"

    # ir
    if verb == "ir":
        forms = {
            "yo": "voy", "tú": "vas", "él/ella": "va",
            "nosotros": "vamos", "vosotros": "vais", "ellos": "van"
        }
        return f"{person} {forms[person]}"

    # ser
    if verb == "ser":
        forms = {
            "yo": "soy", "tú": "eres", "él/ella": "es",
            "nosotros": "somos", "vosotros": "sois", "ellos": "son"
        }
        return f"{person} {forms[person]}"

    # volver (o→ue)
    if verb == "volver" and person in ["yo", "tú", "él/ella", "ellos"]:
        return f"{person} vuelv{ 'o' if person=='yo' else ('es' if person=='tú' else ('e' if person=='él/ella' else 'en')) }"

    # dormir (o→ue)
    if verb == "dormir" and person in ["yo", "tú", "él/ella", "ellos"]:
        stem = "duerm"
        endings = {"yo": "o", "tú": "es", "él/ella": "e", "ellos": "en"}
        return f"{person} {stem}{endings[person]}"

    # elegir (e→i + yo elijo)
    if verb == "elegir":
        if person == "yo":
            return "yo elijo"
        if person in ["tú", "él/ella", "ellos"]:
            stem = "elig".replace("e", "i", 1)
            endings = {"tú": "es", "él/ella": "e", "ellos": "en"}
            return f"{person} {stem}{endings[person]}"

    # seguir (e→i + yo sigo)
    if verb == "seguir":
        if person == "yo":
            return "yo sigo"
        if person in ["tú", "él/ella", "ellos"]:
            stem = "sig"
            endings = {"tú": "ues", "él/ella": "ue", "ellos": "uen"}
            return f"{person} {stem}{endings[person]}"

    # construir (i→y)
    if verb == "construir":
        if person in ["yo", "tú", "él/ella", "ellos"]:
            forms = {
                "yo": "construyo", "tú": "construyes", "él/ella": "construye",
                "nosotros": "construimos", "vosotros": "construís", "ellos": "construyen"
            }
            return f"{person} {forms[person]}"

    # traer
    if verb == "traer" and person == "yo":
        return "yo traigo"

    # conducir
    if verb == "conducir" and person == "yo":
        return "yo conduzco"

    # fallback regular
    stem = verb[:-2]
    ending = verb[-2:]
    if ending == "ar":
        endings = {"yo": "o", "tú": "as", "él/ella": "a",
                   "nosotros": "amos", "vosotros": "áis", "ellos": "an"}
    elif ending == "er":
        endings = {"yo": "o", "tú": "es", "él/ella": "e",
                   "nosotros": "emos", "vosotros": "éis", "ellos": "en"}
    else:
        endings = {"yo": "o", "tú": "es", "él/ella": "e",
                   "nosotros": "imos", "vosotros": "ís", "ellos": "en"}

    return f"{person} {stem}{endings[person]}"

def conjugate(verb, person, tense):
    stem = verb[:-2]
    ending = verb[-2:]

    # Presente
    if tense == "presente":
        return present_irregular(verb, person)

    # Perfecto
    aux = {
        "yo": "he", "tú": "has", "él/ella": "ha",
        "nosotros": "hemos", "vosotros": "habéis", "ellos": "han"
    }

    participio = {
        "escribir": "escrito",
        "abrir": "abierto",
        "romper": "roto",
        "volver": "vuelto",
        "hacer": "hecho",
        "poner": "puesto",
        "decir": "dicho",
        "ver": "visto"
    }.get(verb, stem + ("ado" if ending == "ar" else "ido"))

    if tense == "perfecto":
        return f"{person} {aux[person]} {participio}"

    # Imperfecto (onregelmatig voor ir, ser, ver)
    if tense == "imperfecto":
        if verb == "ir":
            forms = {"yo": "iba", "tú": "ibas", "él/ella": "iba",
                     "nosotros": "íbamos", "vosotros": "ibais", "ellos": "iban"}
            return f"{person} {forms[person]}"
        if verb == "ser":
            forms = {"yo": "era", "tú": "eras", "él/ella": "era",
                     "nosotros": "éramos", "vosotros": "erais", "ellos": "eran"}
            return f"{person} {forms[person]}"
        if verb == "ver":
            forms = {"yo": "veía", "tú": "veías", "él/ella": "veía",
                     "nosotros": "veíamos", "vosotros": "veíais", "ellos": "veían"}
            return f"{person} {forms[person]}"

        # regular fallback
        if ending == "ar":
            endings = {"yo": "aba", "tú": "abas", "él/ella": "aba",
                       "nosotros": "ábamos", "vosotros": "abais", "ellos": "aban"}
        else:
            endings = {"yo": "ía", "tú": "ías", "él/ella": "ía",
                       "nosotros": "íamos", "vosotros": "íais", "ellos": "ían"}
        return f"{person} {stem}{endings[person]}"

    # Gerundio
    if tense == "gerundio":
        if verb == "leer":
            return f"{person} leyendo"
        if verb == "oír":
            return f"{person} oyendo"
        if verb == "construir":
            return f"{person} construyendo"
        if verb == "decir":
            return f"{person} diciendo"
        if verb == "venir":
            return f"{person} viniendo"
        if verb == "dormir":
            return f"{person} durmiendo"
        if ending == "ar":
            return f"{person} {stem}ando"
        else:
            return f"{person} {stem}iendo"


print("=== HARD TRAINER — PILOT v1 ===")

while True:
    verb = random.choice(verbs)
    person = random.choice(persons)
    tense = random.choice(tenses)

    print("\n----------------------------------")
    print(f"Infinitief: {verb}")
    print(f"Persoon: {person}")
    print(f"Tijd: {tense}")
    print("----------------------------------")

    correct = conjugate(verb, person, tense)

    user_form = input("Typ de juiste vorm: ").strip().lower()

    if user_form == correct.lower():
        print("✔ Correct!")
    else:
        print(f"✖ Fout. Correct is: {correct}")

    input("Spreek het hardop uit en druk op Enter...")

    print("\nMaak nu een zin met deze vorm.")
    user_sentence = input("Jouw zin: ").lower()

    if correct.split()[1] in user_sentence or correct in user_sentence:
        print("✔ Zin lijkt correct!")
    else:
        print("⚠ Ik zie de vorm niet terug in je zin.")

    input("Spreek de zin hardop uit en druk op Enter...")

    input("\nDruk op Enter voor de volgende opdracht...")
