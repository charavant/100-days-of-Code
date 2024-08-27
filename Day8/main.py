def greet(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")
    
def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    
    combined_name = name1 + name2
    
    t_count = combined_name.count("t")
    r_count = combined_name.count("r")
    u_count = combined_name.count("u")
    e_count = combined_name.count("e")
    
    true = t_count + r_count + u_count + e_count
    
    l_count = combined_name.count("l")
    o_count = combined_name.count("o")
    v_count = combined_name.count("v")
    e_count = combined_name.count("e")
    
    love = l_count + o_count + v_count + e_count
    
    love_score = int(str(true) + str(love))
    
    print(f"Your love score is {love_score}")

