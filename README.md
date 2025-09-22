# Daniel's One Stop Tile Shop (Python)
A simple Python console app that generates a customer invoice and delivery rate table for a tile shop. It mirrors a university assignment spec and is portfolio‑ready for GitHub.

## Features
- Computes tiles (including +10% extra), grout bags, and thinset bags.
- Adds VAT at 12.5% and prints a clean invoice similar to the sample.
- Prints delivery rate table for distances 5..50 km (step 5): `Total = BaseCharge + $4 * distance`.

## Run
```bash
python tile_shop.py
```

## Inputs
1. Room width (ft)
2. Room length (ft)
3. Tile width (in)
4. Tile length (in)
5. Cost per tile ($)
6. Base delivery charge ($) for destinations within 50 km

## Assumptions & Formulas
- Room and tiles are rectangular.
- Tile area (ft²) = (tileW_in * tileL_in) / 144.
- Tiles = ceil((roomArea / tileArea) * 1.10).
- Grout: 0.13 lb/ft²; 25 lb bags @ $80 → bags = ceil(total_lb / 25).
- Thinset: 90 ft² coverage/bag @ $50 → bags = ceil(roomArea / 90).
- VAT = 12.5% of overall total.
- Delivery total = BaseCharge + $4 × distance (km).

## Example (matches the sample invoice)
```
Enter room width  (feet): 12
Enter room length (feet): 14
Enter tile width  (inches): 12
Enter tile length (inches): 12
Enter cost per tile ($): 9.75
...
Bill Amount:  2,563.59
```
