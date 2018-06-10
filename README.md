## OSRS Unfinished Potions Profit Calculator 
Just revamped this to make it less horrific to look at, and because I've found it useful again!

### Yeah, but what is it?
Running this script will give you information about any herb that you wish to turn into an unfinished potion for profit. [Here's an example of the money making method that this assists with.](http://oldschoolrunescape.wikia.com/wiki/Money_making_guide/Making_ranarr_potions)

### Usage
`python3 potions.py [herb name]`

If using linux it'd be useful to `chmod +x potions.py`.
After that you can `./potions.py [herb name]` i.e. `./potions.py tarromin`.

It should spit out information that looks like this:
```
Tarromin
Buy: 239
Sell: 460
Profit: 216
Buy/Sell Qty: (138/3)
------------------------------
```

Note that if you don't supply an herb, it's going to spit out `Tarromin` through `Kwuarm` in the above format as that is what is profitable and what I'm capable of creating (in-game) at the time of this writing.
