'''
dnSpy-net-win64 SpellBrewery.dll

private static void BrewSpell()
{
	bool flag = Brewery.recipe.Count < 1;
	if (flag)
	{
		Console.WriteLine("You can't brew with an empty cauldron");
	}
	else
	{
		byte[] bytes = (from ing in Brewery.recipe
		select (byte)(Array.IndexOf<string>(Brewery.IngredientNames, ing.ToString()) + 32)).ToArray<byte>();
		bool flag2 = Brewery.recipe.SequenceEqual(from name in Brewery.correct
		select new Ingredient(name));
		if (flag2)
		{
			Console.WriteLine("The spell is complete - your flag is: " + Encoding.ASCII.GetString(bytes));
			Environment.Exit(0);
		}
		else
		{
			Console.WriteLine("The cauldron bubbles as your ingredients melt away. Try another recipe.");
		}
	}
}
'''
correct = [ "Phantom Firefly Wing", "Ghastly Gourd", "Hocus Pocus Powder", "Spider Sling Silk", "Goblin's Gold", "Wraith's Tear", "Werewolf Whisker", "Ghoulish Goblet", "Cursed Skull", "Dragon's Scale Shimmer", "Raven Feather", "Dragon's Scale Shimmer", "Ghoulish Goblet", "Cursed Skull", "Raven Feather", "Spectral Spectacles", "Dragon's Scale Shimmer", "Haunted Hay Bale", "Wraith's Tear", "Zombie Zest Zest", "Serpent Scale", "Wraith's Tear", "Cursed Crypt Key", "Dragon's Scale Shimmer", "Salamander's Tail", "Raven Feather", "Wolfsbane", "Frankenstein's Lab Liquid", "Zombie Zest Zest", "Cursed Skull", "Ghoulish Goblet", "Dragon's Scale Shimmer", "Cursed Crypt Key", "Wraith's Tear", "Black Cat's Meow", "Wraith Whisper" ]

IngredientNames = [ "Witch's Eye", "Bat Wing", "Ghostly Essence", "Toadstool Extract", "Vampire Blood", "Mandrake Root", "Zombie Brain", "Ghoul's Breath", "Spider Venom", "Black Cat's Whisker", "Werewolf Fur", "Banshee's Wail", "Spectral Ash", "Pumpkin Spice", "Goblin's Earwax", "Haunted Mist", "Wraith's Tear", "Serpent Scale", "Moonlit Fern", "Cursed Skull", "Raven Feather", "Wolfsbane", "Frankenstein's Bolt", "Wicked Ivy", "Screaming Banshee Berry", "Mummy's Wrappings", "Dragon's Breath", "Bubbling Cauldron Brew", "Gorehound's Howl", "Wraithroot", "Haunted Grave Moss", "Ectoplasmic Slime", "Voodoo Doll's Stitch", "Bramble Thorn", "Hocus Pocus Powder", "Cursed Clove", "Wicked Witch's Hair", "Halloween Moon Dust", "Bog Goblin Slime", "Ghost Pepper", "Phantom Firefly Wing", "Gargoyle Stone", "Zombie Toenail", "Poltergeist Polyp", "Spectral Goo", "Salamander Scale", "Cursed Candelabra Wax", "Witch Hazel", "Banshee's Bane", "Grim Reaper's Scythe", "Black Widow Venom", "Moonlit Nightshade", "Ghastly Gourd", "Siren's Song Seashell", "Goblin Gold Dust", "Spider Web Silk", "Haunted Spirit Vine", "Frog's Tongue", "Mystic Mandrake", "Widow's Peak Essence", "Wicked Warlock's Beard", "Crypt Keeper's Cryptonite", "Bewitched Broomstick Bristle", "Dragon's Scale Shimmer", "Vampire Bat Blood", "Graveyard Grass", "Halloween Harvest Pumpkin", "Cursed Cobweb Cotton", "Phantom Howler Fur", "Wraithbone", "Goblin's Green Slime", "Witch's Brew Brew", "Voodoo Doll Pin", "Bramble Berry", "Spooky Spellbook Page", "Halloween Cauldron Steam", "Spectral Spectacles", "Salamander's Tail", "Cursed Crypt Key", "Pumpkin Patch Spice", "Haunted Hay Bale", "Banshee's Bellflower", "Ghoulish Goblet", "Frankenstein's Lab Liquid", "Zombie Zest Zest", "Werewolf Whisker", "Gargoyle Gaze", "Black Cat's Meow", "Wolfsbane Extract", "Goblin's Gold", "Phantom Firefly Fizz", "Spider Sling Silk", "Widow's Weave", "Wraith Whisper", "Siren's Serenade", "Moonlit Mirage", "Spectral Spark", "Dragon's Roar", "Banshee's Banshee", "Witch's Whisper", "Ghoul's Groan", "Toadstool Tango", "Vampire's Kiss", "Bubbling Broth", "Mystic Elixir", "Cursed Charm" ]

flag = ''
for i in correct:
	if i in IngredientNames:
		flag += chr(IngredientNames.index(i)+32)

print(flag)

