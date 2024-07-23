import random

def secret_santa(names):
    if len(names) < 2:
        return "List must contain at least two names."
    
    givers = names[:]
    receivers = names[:]
    
    while True:
        random.shuffle(receivers)
        # Ensure no one is assigned to themselves
        if all(giver != receiver for giver, receiver in zip(givers, receivers)):
            break
    
    pairs = list(zip(givers, receivers))
    
    # Format the output as specified
    result = "\n".join(f"{giver} -> {receiver}" for giver, receiver in pairs)
    return result

names = ["Χαράλαμπος", "Άγγελος", "Αλέξανδρος", "Βασίλης", 
         "Γιάννης", "Γιώργος", "Βαγγέλης", "Λουκάς", 
         "Μιχάλης", "Νικήτας", "Νίκος Κ", "Νίκος Μ", 
         "Παναγιώτης", "Σάκης", "Σπύρος", "Στέφανος", "Στάθης"]
santa_pairs = secret_santa(names)
print(santa_pairs)
