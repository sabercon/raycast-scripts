from dataclasses import dataclass, fields
from typing import Self


@dataclass(frozen=True)
class Nutrient:
    # Macronutrient
    calories: float = 0.0
    protein: float = 0.0
    carbs: float = 0.0
    fat: float = 0.0
    fiber: float = 0.0

    # Vitamin
    vitamin_a_mcg: float = 0.0
    vitamin_c_mg: float = 0.0
    vitamin_d_mcg: float = 0.0
    vitamin_e_mg: float = 0.0
    vitamin_k_mcg: float = 0.0
    vitamin_b1_mg: float = 0.0  # Thiamine
    vitamin_b2_mg: float = 0.0  # Riboflavin
    vitamin_b3_mg: float = 0.0  # Niacin
    vitamin_b5_mg: float = 0.0  # Pantothenic Acid
    vitamin_b6_mg: float = 0.0  # Pyridoxine
    vitamin_b7_mcg: float = 0.0  # Biotin
    vitamin_b9_mcg: float = 0.0  # Folate
    vitamin_b12_mcg: float = 0.0  # Cobalamin
    choline_mg: float = 0.0

    # Mineral
    calcium_mg: float = 0.0
    copper_mg: float = 0.0
    iodine_mcg: float = 0.0
    iron_mg: float = 0.0
    magnesium_mg: float = 0.0
    phosphorus_mg: float = 0.0
    potassium_mg: float = 0.0
    selenium_mcg: float = 0.0
    sodium_mg: float = 0.0
    zinc_mg: float = 0.0

    def __add__(self, other: Self) -> Self:
        return self.__class__(**{f.name: getattr(self, f.name) + getattr(other, f.name) for f in fields(self)})

    def __mul__(self, factor: float) -> Self:
        return self.__class__(**{f.name: getattr(self, f.name) * factor for f in fields(self)})

    def __rmul__(self, factor: float) -> Self:
        return self.__mul__(factor)


def print_summary(intake: Nutrient, target: Nutrient) -> None:
    for field in fields(intake):
        i = getattr(intake, field.name)
        t = getattr(target, field.name)
        pct = i / t * 100
        color = '\033[32m' if pct >= 100 else '\033[34m' if pct >= 80 else '\033[31m'
        reset = '\033[0m'
        print(f'{field.name}: {color}{i:g}/{t:g} ({pct:.1f}%){reset}')


def daily_recommended(n: float = 1) -> Nutrient:
    return Nutrient(
        calories=2500,
        protein=130,
        carbs=300,
        fat=65,
        fiber=30,
        vitamin_a_mcg=900,
        vitamin_c_mg=100,
        vitamin_d_mcg=15,
        vitamin_e_mg=15,
        vitamin_k_mcg=120,
        vitamin_b1_mg=1.2,
        vitamin_b2_mg=1.3,
        vitamin_b3_mg=16,
        vitamin_b5_mg=5,
        vitamin_b6_mg=1.3,
        vitamin_b7_mcg=30,
        vitamin_b9_mcg=400,
        vitamin_b12_mcg=2.4,
        choline_mg=550,
        calcium_mg=1000,
        copper_mg=0.9,
        iodine_mcg=150,
        iron_mg=8,
        magnesium_mg=400,
        phosphorus_mg=700,
        potassium_mg=3400,
        selenium_mcg=55,
        sodium_mg=1500,
        zinc_mg=11,
    ) * n


def supplements(n: float = 1) -> Nutrient:
    return Nutrient(
        vitamin_d_mcg=16 * 2 / 3,
        vitamin_k_mcg=60 * 2 / 3,
        calcium_mg=666 * 2 / 3,
        sodium_mg=1000,
        fat=10,
    ) * n


def egg_poached_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/172186/nutrients
    return Nutrient(
        calories=143,
        protein=12.5,
        fat=9.47,
        vitamin_a_mcg=160,
        vitamin_d_mcg=2,
        vitamin_e_mg=1.04,
        vitamin_b1_mg=0.032,
        vitamin_b2_mg=0.387,
        vitamin_b5_mg=1.53,
        vitamin_b6_mg=0.144,
        vitamin_b7_mcg=25,
        vitamin_b9_mcg=35,
        vitamin_b12_mcg=0.71,
        choline_mg=234,
        calcium_mg=56,
        copper_mg=0.072,
        iodine_mcg=22.5,
        iron_mg=1.75,
        magnesium_mg=12,
        phosphorus_mg=197,
        potassium_mg=138,
        selenium_mcg=30.6,
        sodium_mg=297,
        zinc_mg=1.29,
    ) * n


def milk_nonfat_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/173432/nutrients
    return Nutrient(
        calories=35,
        protein=3.37,
        carbs=4.86,
        vitamin_b1_mg=0.045,
        vitamin_b2_mg=0.182,
        vitamin_b5_mg=0.357,
        vitamin_b6_mg=0.037,
        vitamin_b12_mcg=0.5,
        choline_mg=15.6,
        calcium_mg=122,
        magnesium_mg=11,
        phosphorus_mg=101,
        potassium_mg=156,
        selenium_mcg=3.1,
        sodium_mg=42,
        zinc_mg=0.42,
    ) * n


def blueberries_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/171711/nutrients
    return Nutrient(
        calories=57,
        carbs=14.5,
        fiber=2.4,
        vitamin_c_mg=9.7,
        vitamin_e_mg=0.57,
        vitamin_k_mcg=19.3,
        vitamin_b1_mg=0.037,
        vitamin_b2_mg=0.041,
        vitamin_b3_mg=0.418,
        vitamin_b5_mg=0.124,
        vitamin_b6_mg=0.052,
        copper_mg=0.057,
        iron_mg=0.28,
        potassium_mg=77,
    ) * n


def bananas_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/173944/nutrients
    return Nutrient(
        calories=89,
        protein=1.09,
        carbs=22.8,
        fiber=2.6,
        vitamin_c_mg=8.7,
        vitamin_b1_mg=0.031,
        vitamin_b2_mg=0.073,
        vitamin_b3_mg=0.665,
        vitamin_b5_mg=0.334,
        vitamin_b6_mg=0.367,
        vitamin_b9_mcg=20,
        choline_mg=9.8,
        copper_mg=0.078,
        iron_mg=0.26,
        magnesium_mg=27,
        phosphorus_mg=22,
        potassium_mg=358,
        selenium_mcg=1,
    ) * n


def kiwifruit_zespri_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/168211/nutrients
    return Nutrient(
        calories=63,
        protein=1.02,
        carbs=15.8,
        fiber=1.4,
        vitamin_c_mg=161,
        vitamin_e_mg=1.4,
        vitamin_k_mcg=6.1,
        vitamin_b2_mg=0.074,
        vitamin_b5_mg=0.12,
        vitamin_b6_mg=0.079,
        vitamin_b9_mcg=31,
        vitamin_b12_mcg=0.08,
        copper_mg=0.151,
        magnesium_mg=12,
        phosphorus_mg=25,
        potassium_mg=315,
    ) * n


def tomatoes_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/170457/nutrients
    return Nutrient(
        calories=18,
        protein=0.88,
        carbs=3.89,
        fiber=1.2,
        vitamin_a_mcg=42,
        vitamin_c_mg=13.7,
        vitamin_e_mg=0.54,
        vitamin_k_mcg=7.9,
        vitamin_b1_mg=0.037,
        vitamin_b2_mg=0.019,
        vitamin_b3_mg=0.594,
        vitamin_b5_mg=0.089,
        vitamin_b6_mg=0.08,
        vitamin_b9_mcg=15,
        copper_mg=0.059,
        iron_mg=0.27,
        magnesium_mg=11,
        phosphorus_mg=24,
        potassium_mg=237,
    ) * n


def carrots_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/170393/nutrients
    return Nutrient(
        calories=41,
        protein=0.93,
        carbs=9.58,
        fiber=2.8,
        vitamin_a_mcg=835,
        vitamin_c_mg=5.9,
        vitamin_e_mg=0.66,
        vitamin_k_mcg=13.2,
        vitamin_b1_mg=0.066,
        vitamin_b2_mg=0.058,
        vitamin_b3_mg=0.983,
        vitamin_b5_mg=0.273,
        vitamin_b6_mg=0.138,
        vitamin_b9_mcg=19,
        calcium_mg=33,
        copper_mg=0.045,
        iron_mg=0.3,
        magnesium_mg=12,
        phosphorus_mg=35,
        potassium_mg=320,
        sodium_mg=69,
    ) * n


def sweet_potatoes_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/168484/nutrients
    return Nutrient(
        calories=76,
        protein=1.37,
        carbs=17.7,
        fiber=2.5,
        vitamin_a_mcg=787,
        vitamin_c_mg=12.8,
        vitamin_e_mg=0.94,
        vitamin_k_mcg=2.1,
        vitamin_b1_mg=0.056,
        vitamin_b2_mg=0.047,
        vitamin_b3_mg=0.538,
        vitamin_b5_mg=0.581,
        vitamin_b6_mg=0.165,
        vitamin_b9_mcg=6,
        choline_mg=10.8,
        calcium_mg=27,
        copper_mg=0.094,
        iron_mg=0.72,
        magnesium_mg=18,
        phosphorus_mg=32,
        potassium_mg=230,
        sodium_mg=27,
        zinc_mg=0.2,
    ) * n


def broccoli_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/170379/nutrients
    return Nutrient(
        calories=34,
        protein=2.82,
        carbs=6.64,
        fiber=2.6,
        vitamin_a_mcg=31,
        vitamin_c_mg=89.2,
        vitamin_e_mg=0.78,
        vitamin_k_mcg=102,
        vitamin_b1_mg=0.071,
        vitamin_b2_mg=0.117,
        vitamin_b3_mg=0.639,
        vitamin_b5_mg=0.573,
        vitamin_b6_mg=0.175,
        vitamin_b9_mcg=63,
        choline_mg=18.7,
        calcium_mg=47,
        copper_mg=0.049,
        iron_mg=0.73,
        magnesium_mg=21,
        phosphorus_mg=66,
        potassium_mg=316,
        selenium_mcg=2.5,
        zinc_mg=0.41,
    ) * n


def asparagus_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/2710823/nutrients
    return Nutrient(
        calories=28,
        protein=1.44,
        carbs=5.1,
        fiber=1.9,
        vitamin_c_mg=9.2,
        vitamin_b1_mg=0.069,
        vitamin_b3_mg=1.08,
        vitamin_b6_mg=0.112,
        vitamin_b9_mcg=182,
        calcium_mg=21,
        copper_mg=0.132,
        iron_mg=0.44,
        magnesium_mg=13.8,
        phosphorus_mg=54,
        potassium_mg=278,
        zinc_mg=0.6,
    ) * n


def arugula_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/169387/nutrients
    return Nutrient(
        calories=25,
        protein=2.58,
        carbs=3.65,
        fiber=1.6,
        vitamin_a_mcg=119,
        vitamin_c_mg=15,
        vitamin_e_mg=0.43,
        vitamin_k_mcg=109,
        vitamin_b1_mg=0.044,
        vitamin_b2_mg=0.086,
        vitamin_b3_mg=0.305,
        vitamin_b5_mg=0.437,
        vitamin_b6_mg=0.073,
        vitamin_b9_mcg=97,
        choline_mg=15.3,
        calcium_mg=160,
        copper_mg=0.076,
        iron_mg=1.46,
        magnesium_mg=47,
        phosphorus_mg=52,
        potassium_mg=369,
        zinc_mg=0.47,
    ) * n


def peppers_sweet_green_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/170427/nutrients
    return Nutrient(
        calories=20,
        protein=0.86,
        carbs=4.64,
        fiber=1.7,
        vitamin_a_mcg=18,
        vitamin_c_mg=80.4,
        vitamin_e_mg=0.37,
        vitamin_k_mcg=7.4,
        vitamin_b1_mg=0.057,
        vitamin_b2_mg=0.028,
        vitamin_b3_mg=0.48,
        vitamin_b5_mg=0.099,
        vitamin_b6_mg=0.224,
        vitamin_b9_mcg=10,
        copper_mg=0.066,
        iron_mg=0.34,
        magnesium_mg=10,
        phosphorus_mg=20,
        potassium_mg=175,
    ) * n


def peppers_sweet_red_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/170108/nutrients
    return Nutrient(
        calories=26,
        protein=0.99,
        carbs=6.03,
        fiber=2.1,
        vitamin_a_mcg=157,
        vitamin_c_mg=128,
        vitamin_e_mg=1.58,
        vitamin_k_mcg=4.9,
        vitamin_b1_mg=0.054,
        vitamin_b2_mg=0.085,
        vitamin_b3_mg=0.979,
        vitamin_b5_mg=0.317,
        vitamin_b6_mg=0.291,
        vitamin_b9_mcg=46,
        copper_mg=0.017,
        iron_mg=0.43,
        magnesium_mg=12,
        phosphorus_mg=26,
        potassium_mg=211,
    ) * n


def peppers_sweet_yellow_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/169383/nutrients
    return Nutrient(
        calories=27,
        protein=1,
        carbs=6.32,
        fiber=0.9,
        vitamin_a_mcg=10,
        vitamin_c_mg=184,
        vitamin_b1_mg=0.028,
        vitamin_b2_mg=0.025,
        vitamin_b3_mg=0.89,
        vitamin_b5_mg=0.168,
        vitamin_b6_mg=0.168,
        vitamin_b9_mcg=26,
        copper_mg=0.107,
        iron_mg=0.46,
        magnesium_mg=12,
        phosphorus_mg=24,
        potassium_mg=212,
    ) * n


def chicken_breast_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/171477/nutrientsdd
    return Nutrient(
        calories=94,
        protein=21.2,
        fat=0.9,
        vitamin_b1_mg=0.07,
        vitamin_b2_mg=0.114,
        vitamin_b3_mg=13.7,
        vitamin_b5_mg=0.965,
        vitamin_b6_mg=0.6,
        vitamin_b7_mcg=3.6,
        vitamin_b12_mcg=0.34,
        choline_mg=85.3,
        copper_mg=0.049,
        iodine_mcg=3.2,
        iron_mg=1.04,
        magnesium_mg=29,
        phosphorus_mg=228,
        potassium_mg=256,
        selenium_mcg=27.6,
        sodium_mg=328,
        zinc_mg=1,
    ) * n


def salmon_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/175167/nutrients
    return Nutrient(
        calories=263,
        protein=17.8,
        fat=21.6,
        vitamin_a_mcg=58,
        vitamin_d_mcg=11,
        vitamin_e_mg=3.55,
        vitamin_b1_mg=0.207,
        vitamin_b2_mg=0.155,
        vitamin_b3_mg=8.67,
        vitamin_b5_mg=1.55,
        vitamin_b6_mg=0.636,
        vitamin_b7_mcg=9,
        vitamin_b9_mcg=26,
        vitamin_b12_mcg=3.23,
        choline_mg=78.5,
        copper_mg=0.045,
        iodine_mcg=10,
        iron_mg=0.34,
        magnesium_mg=27,
        phosphorus_mg=240,
        potassium_mg=363,
        selenium_mcg=24,
        sodium_mg=100,
        zinc_mg=0.36,
    ) * n


def steak_lean_100g(n: float = 1) -> Nutrient:
    # https://fdc.nal.usda.gov/food-details/169429/nutrients
    return Nutrient(
        calories=117,
        protein=23.1,
        fat=2.69,
        vitamin_b1_mg=0.052,
        vitamin_b2_mg=0.124,
        vitamin_b3_mg=6.7,
        vitamin_b5_mg=0.678,
        vitamin_b6_mg=0.651,
        vitamin_b7_mcg=2,
        vitamin_b9_mcg=13,
        vitamin_b12_mcg=1.27,
        choline_mg=65.1,
        copper_mg=0.068,
        iodine_mcg=4.1,
        iron_mg=1.85,
        magnesium_mg=23,
        phosphorus_mg=212,
        potassium_mg=342,
        selenium_mcg=21.1,
        sodium_mg=55,
        zinc_mg=3.61,
    ) * n


def nuts_mixed_100g(n: float = 1) -> Nutrient:
    return Nutrient(
        calories=668.5,
        protein=19.3,
        carbs=10.8,
        fat=60.5,
        fiber=5.8,
        vitamin_e_mg=6.89,
        iron_mg=3.7,
        magnesium_mg=198,
        phosphorus_mg=423,
        potassium_mg=578,
        zinc_mg=3.41,
    ) * n


def rice_mixed_100g(n: float = 1) -> Nutrient:
    return Nutrient(
        calories=348.7,
        protein=10,
        carbs=67.4,
        fat=2.3,
        fiber=7.3,
        vitamin_b1_mg=0.3,
        calcium_mg=36,
        iron_mg=1.9,
        magnesium_mg=81,
        phosphorus_mg=207,
        potassium_mg=415,
        zinc_mg=1.72,
    ) * n


def oats_black_100g(n: float = 1) -> Nutrient:
    return Nutrient(
        calories=376.4,
        protein=12,
        carbs=56.8,
        fat=8.8,
        fiber=10,
        vitamin_b1_mg=0.17,
        vitamin_b3_mg=2.1,
        vitamin_b6_mg=0.11,
        calcium_mg=60,
        iron_mg=2.3,
        magnesium_mg=90,
        phosphorus_mg=210,
        potassium_mg=300,
        zinc_mg=1.3,
    ) * n


def oats_probiotics_100g(n: float = 1) -> Nutrient:
    return Nutrient(
        calories=382,
        protein=8,
        carbs=56.8,
        fat=11.5,
        fiber=9,
        vitamin_b1_mg=0.2,
        magnesium_mg=94,
        phosphorus_mg=186,
        potassium_mg=468,
    ) * n


def seaweed_snack(n: float = 1) -> Nutrient:
    return Nutrient(
        calories=565,
        protein=26.5,
        fat=46.8,
        fiber=18.8,
        vitamin_e_mg=15,
        calcium_mg=512,
        iodine_mcg=2000,
        iron_mg=7.8,
        magnesium_mg=222,
        sodium_mg=512,
        zinc_mg=3.74,
    ) * n


def bread_milk_high_calcium_100g(n: float = 1) -> Nutrient:
    return Nutrient(
        calories=314,
        protein=11.1,
        carbs=51,
        fat=7,
        calcium_mg=265,
        sodium_mg=310,
    ) * n


if __name__ == '__main__':
    breakfast = oats_probiotics_100g(0.4) + egg_poached_100g(1) + blueberries_100g(1)
    other = supplements(1) + milk_nonfat_100g(2)

    regular_lunch = rice_mixed_100g(0.8) + salmon_100g(2) + carrots_100g(2)
    regular_dinner = rice_mixed_100g(0.8) + chicken_breast_100g(0.9) + kiwifruit_zespri_100g(1)
    regular_day = breakfast + other + regular_lunch + regular_dinner

    workout_lunch = sweet_potatoes_100g(1.5) + steak_lean_100g(1.8) + arugula_100g(1) + nuts_mixed_100g(0.25)
    workout_dinner = rice_mixed_100g(0.8) + chicken_breast_100g(0.9) + seaweed_snack(0.075) + bananas_100g(1.5)
    workout_day = breakfast + other + workout_lunch + workout_dinner

    # print_summary(regular_day, daily_recommended())
    # print_summary(workout_day, daily_recommended())
    print_summary(regular_day * (2 / 5) + workout_day * (3 / 5), daily_recommended())
