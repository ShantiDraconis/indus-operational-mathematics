"""
Example: Calendar calculations in Mayan and Aztec systems.

This script demonstrates calendar operations that show
the operational mathematics underlying these systems.
"""

import sys
sys.path.insert(0, 'src')

from symbolic_systems import MayanSystem, AztecSystem


def main():
    print("=" * 70)
    print("Mesoamerican Calendar Systems")
    print("=" * 70)
    print()
    
    # Mayan Calendar
    print("1. MAYAN CALENDAR SYSTEM")
    print()
    mayan = MayanSystem()
    
    print("   System Parameters:")
    print(f"      Tzolk'in (sacred): {mayan.calendar['tzolkin_days']} days")
    print(f"      Haab' (solar): {mayan.calendar['haab_days']} days")
    print(f"      Day signs: {mayan.calendar['day_signs']}")
    print(f"      Day numbers: {mayan.calendar['day_numbers']}")
    print()
    
    print("   Example Date Calculations:")
    
    # Calculate some example dates
    dates = [
        {'kin': 5, 'uinal': 0, 'tun': 0},
        {'kin': 0, 'uinal': 1, 'tun': 0},
        {'kin': 0, 'uinal': 0, 'tun': 1},
        {'kin': 13, 'uinal': 9, 'tun': 2},
    ]
    
    for date_params in dates:
        result = mayan.calculate_calendar_date(**date_params)
        print(f"      {date_params['kin']} K'in + {date_params['uinal']} Uinal + {date_params['tun']} Tun")
        print(f"         = {result['total_days']} days")
        print(f"         Tzolk'in position: day {result['tzolkin_day']} of {mayan.calendar['tzolkin_days']}")
        print(f"         Haab' position: day {result['haab_day']} of {mayan.calendar['haab_days']}")
        print()
    
    # Aztec Calendar
    print("2. AZTEC CALENDAR SYSTEM")
    print()
    aztec = AztecSystem()
    
    print("   System Parameters:")
    print(f"      Tonalpohualli (sacred): {aztec.calendar['tonalpohualli_days']} days")
    print(f"      Day signs: {aztec.calendar['day_signs']}")
    print(f"      Day numbers: {aztec.calendar['day_numbers']}")
    print()
    
    print("   The 20 Day Signs:")
    for i, sign in enumerate(aztec.day_signs, 1):
        print(f"      {i:2d}. {sign}")
    print()
    
    print("   Example Tonalpohualli Dates:")
    
    # Calculate some example Tonalpohualli dates
    tonalpohualli_examples = [
        {'day_number': 1, 'day_sign_index': 0},
        {'day_number': 7, 'day_sign_index': 3},
        {'day_number': 13, 'day_sign_index': 19},
    ]
    
    for params in tonalpohualli_examples:
        result = aztec.calculate_tonalpohualli(**params)
        print(f"      {result['representation']}")
        print(f"         Position in 260-day cycle: {result['calendar_position']}")
        print()
    
    # Show the combinatorial nature
    print("3. COMBINATORIAL STRUCTURE")
    print()
    print("   Both systems use combinatorial principles:")
    print(f"      Mayan: {mayan.calendar['day_signs']} signs × {mayan.calendar['day_numbers']} numbers = {mayan.calendar['tzolkin_days']} unique combinations")
    print(f"      Aztec: {aztec.calendar['day_signs']} signs × {aztec.calendar['day_numbers']} numbers = {aztec.calendar['tonalpohualli_days']} unique combinations")
    print()
    print("   This is isomorphic to Harappan structure:")
    print("      20 base symbols × 13 numeric modifiers = composite system")
    print()
    
    # Show parallel with operational mathematics
    print("4. OPERATIONAL INTERPRETATION")
    print()
    print("   Mayan Date Structure:")
    print("      Date = Temporal_Entity ⊕ Quantifier ⊕ Cycle ⊕ Closure")
    print()
    print("   Aztec Tonalpohualli:")
    print("      Date = Day_Number ⊕ Day_Sign")
    print("      Position = Combinatorial_State(number, sign)")
    print()
    
    print("=" * 70)
    print("Calendar Analysis Complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
