colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
           "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
           "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour = input("Enter a colour ")
while colour != "":
    print(colours.get(colour))
    colour = input("Enter a colour ")

