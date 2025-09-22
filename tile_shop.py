"""
Daniel's One Stop Tile Shop (Python)
------------------------------------
Console app to generate an invoice and a delivery-rate table.
Implements the exact rules from the assignment spec.

Usage
-----
python tile_shop.py
"""

from math import ceil

VAT_RATE = 0.125                # 12.5%
EXTRA_TILES_FACTOR = 1.10       # +10%
IN2_PER_FT2 = 144.0

# Grout
GROUT_LB_PER_FT2 = 0.13
GROUT_BAG_LB = 25.0
GROUT_BAG_COST = 80.0

# Thinset
THINSET_BAG_COVERAGE_FT2 = 90.0
THINSET_BAG_COST = 50.0

def generate_invoice(room_w_ft: float,
                     room_l_ft: float,
                     tile_w_in: float,
                     tile_l_in: float,
                     tile_unit_cost: float):
    """Return a dict with all computed invoice fields."""
    room_area_ft2 = room_w_ft * room_l_ft
    tile_area_ft2 = (tile_w_in * tile_l_in) / IN2_PER_FT2

    # Tiles
    tiles_needed_exact = (room_area_ft2 / tile_area_ft2) * EXTRA_TILES_FACTOR
    tiles_qty = int(ceil(tiles_needed_exact))
    tiles_subtotal = tiles_qty * tile_unit_cost

    # Grout
    grout_lb_total = room_area_ft2 * GROUT_LB_PER_FT2
    grout_bags = int(ceil(grout_lb_total / GROUT_BAG_LB))
    grout_subtotal = grout_bags * GROUT_BAG_COST

    # Thinset
    thinset_bags = int(ceil(room_area_ft2 / THINSET_BAG_COVERAGE_FT2))
    thinset_subtotal = thinset_bags * THINSET_BAG_COST

    total_before_vat = tiles_subtotal + grout_subtotal + thinset_subtotal
    vat = total_before_vat * VAT_RATE
    bill = total_before_vat + vat

    return {
        "tiles_qty": tiles_qty,
        "grout_bags": grout_bags,
        "thinset_bags": thinset_bags,
        "tiles_unit_cost": tile_unit_cost,
        "grout_unit_cost": GROUT_BAG_COST,
        "thinset_unit_cost": THINSET_BAG_COST,
        "tiles_subtotal": tiles_subtotal,
        "grout_subtotal": grout_subtotal,
        "thinset_subtotal": thinset_subtotal,
        "total_before_vat": total_before_vat,
        "vat": vat,
        "bill": bill,
    }

def print_invoice(inv: dict) -> None:
    """Pretty-print the invoice to the console in the sample style."""
    def money(x): return f"{x:,.2f}"

    print("DANIEL'S ONE STOP TILE SHOP")
    print("INVOICE")
    print(f'{"ITEM":24}{"QTY":>6}{"UNIT COST":>12}{"SUBTOTAL":>12}')
    print("-" * (24 + 6 + 12 + 12))

    def line(name, qty, unit, subtotal):
        print(f"{name:24}{qty:>6}{money(unit):>12}{money(subtotal):>12}")

    line("Tiles",   inv["tiles_qty"],    inv["tiles_unit_cost"],   inv["tiles_subtotal"])
    line("Grout",   inv["grout_bags"],   inv["grout_unit_cost"],   inv["grout_subtotal"])
    line("Thinset", inv["thinset_bags"], inv["thinset_unit_cost"], inv["thinset_subtotal"])

    # Right-aligned totals
    total_line_width = 24 + 6 + 12 + 12
    def right(label, value):
        s = f"{label}  {money(value)}"
        print(" " * (total_line_width - len(s)) + s)

    print()
    right("Total Cost:", inv["total_before_vat"])
    right("VAT (12.5%):", inv["vat"])
    right("Bill Amount:", inv["bill"])
    print()
    print("WE ACCEPT CASH, LINX, OR CREDIT CARD FOR YOUR CONVENIENCE")
    print()

def print_delivery_table(base_charge: float) -> None:
    """Print the delivery rate table from 5 to 50 km in steps of 5 km."""
    print("DELIVERY RATES (within 50 km)")
    print(f'{"Distance":10}{"Base Charge":14}{"Surcharge":12}{"Total":10}')
    print("-" * (10 + 14 + 12 + 10))

    for km in range(5, 51, 5):
        surcharge = 4.0 * km
        total = base_charge + surcharge
        print(f"{str(km)+' km':10}{base_charge:14.2f}{surcharge:12.2f}{total:10.2f}")

def main():
    print("=== Daniel's One Stop Tile Shop ===\n")

    try:
        room_w_ft = float(input("Enter room width  (feet): ").strip())
        room_l_ft = float(input("Enter room length (feet): ").strip())
        tile_w_in = float(input("Enter tile width  (inches): ").strip())
        tile_l_in = float(input("Enter tile length (inches): ").strip())
        tile_cost = float(input("Enter cost per tile ($): ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    inv = generate_invoice(room_w_ft, room_l_ft, tile_w_in, tile_l_in, tile_cost)
    print()
    print_invoice(inv)

    try:
        base_delivery = float(input("Enter base delivery charge for <=50 km ($): ").strip())
    except ValueError:
        print("Invalid input. Skipping delivery table.")
        return

    print()
    print_delivery_table(base_delivery)
    print()

if __name__ == "__main__":
    main()
