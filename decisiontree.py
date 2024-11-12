def diagnose():
    print("Welcome to the Medical Expert System!")
    print("Answer the following questions with 'yes' or 'no'.\n")

    # Start of decision tree
    fever = input("Do you have a fever? ").strip().lower()
    
    if fever == "yes":
        body_aches = input("Do you have body aches? ").strip().lower()
        if body_aches == "yes":
            print("Diagnosis: You may have the Flu.")
        else:
            print("Diagnosis: You may have a Common Cold.")
    
    elif fever == "no":
        sneezing = input("Are you sneezing frequently? ").strip().lower()
        if sneezing == "yes":
            print("Diagnosis: You may have Allergies.")
        else:
            print("Diagnosis: You may have a Common Cold.")

    else:
        print("Please answer with 'yes' or 'no'.")

# Run the expert system
diagnose()
