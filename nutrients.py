from dataclasses import dataclass, field, fields
from typing import Self


def _untracked() -> float:
    # Deficiency is rare, so this field is excluded from the summary
    return field(default=0.0, metadata={'untracked': True})


@dataclass(frozen=True)
class Nutrient:
    # Macronutrient
    protein: float = 0.0
    carbs: float = 0.0
    fat: float = 0.0
    fiber: float = 0.0

    # Vitamin
    vitamin_a_mcg: float = 0.0
    vitamin_c_mg: float = 0.0
    vitamin_d_mcg: float = 0.0
    vitamin_e_mg: float = _untracked()
    vitamin_k_mcg: float = _untracked()
    vitamin_b1_mg: float = 0.0  # Thiamine
    vitamin_b2_mg: float = 0.0  # Riboflavin
    vitamin_b3_mg: float = _untracked()  # Niacin
    vitamin_b5_mg: float = _untracked()  # Pantothenic Acid
    vitamin_b6_mg: float = 0.0  # Pyridoxine
    vitamin_b7_mcg: float = _untracked()  # Biotin
    vitamin_b9_mcg: float = 0.0  # Folate
    vitamin_b12_mcg: float = _untracked()  # Cobalamin
    choline_mg: float = _untracked()

    # Mineral
    calcium_mg: float = 0.0
    iodine_mcg: float = 0.0
    iron_mg: float = 0.0
    magnesium_mg: float = 0.0
    phosphorus_mg: float = 0.0  # The less, the better
    potassium_mg: float = 0.0
    selenium_mcg: float = _untracked()
    sodium_mg: float = 0.0  # The less, the better
    zinc_mg: float = 0.0

    @property
    def calories(self) -> float:
        # Atwater factors: 4 cal/g protein and carbs, 9 cal/g fat
        return self.protein * 4 + self.carbs * 4 + self.fat * 9

    def __add__(self, other: Self) -> Self:
        return self.__class__(**{f.name: getattr(self, f.name) + getattr(other, f.name) for f in fields(self)})

    def __mul__(self, factor: float) -> Self:
        return self.__class__(**{f.name: getattr(self, f.name) * factor for f in fields(self)})

    def __rmul__(self, factor: float) -> Self:
        return self.__mul__(factor)


def print_summary(intake: Nutrient, target: Nutrient, show_untracked: bool = False) -> None:
    shown = [f.name for f in fields(intake) if show_untracked or not f.metadata.get('untracked')]
    for name in ['calories', *shown]:
        i = getattr(intake, name)
        t = getattr(target, name)
        pct = i / t * 100
        color = '\033[32m' if pct >= 100 else '\033[34m' if pct >= 80 else '\033[31m'
        reset = '\033[0m'
        print(f'{name}: {color}{i:g}/{t:g} ({pct:.1f}%){reset}')


def daily_recommended(n: float = 1) -> Nutrient:
    # https://www.nal.usda.gov/human-nutrition-and-food-safety/dri-calculator
    return Nutrient(
        protein=120,  # 2g/kg
        carbs=250,  # 4g/kg
        fat=60,  # 1g/kg
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
        vitamin_d_mcg=5.55 * 2,
        vitamin_k_mcg=20 * 2,
        calcium_mg=222.22 * 2,
    ) * n


def protein_powder_100g(n: float = 1) -> Nutrient:
    return Nutrient(
        protein=88,
        carbs=2.8,
        fat=0.4,
        vitamin_a_mcg=650,
        vitamin_b1_mg=5.33,
        vitamin_b2_mg=2.67,
        vitamin_b6_mg=2.67,
        zinc_mg=17.91,
    ) * n


def eggs_hard_boiled_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/173424
    return Nutrient(
        protein=12.6,
        carbs=1.1,
        fat=10.6,
        vitamin_a_mcg=149,
        vitamin_d_mcg=2.2,
        vitamin_e_mg=1,
        vitamin_k_mcg=0.3,
        vitamin_b1_mg=0.07,
        vitamin_b2_mg=0.51,
        vitamin_b3_mg=0.06,
        vitamin_b5_mg=1.4,
        vitamin_b6_mg=0.12,
        vitamin_b7_mcg=20,
        vitamin_b9_mcg=44,
        vitamin_b12_mcg=1.1,
        choline_mg=293.8,
        calcium_mg=50,
        iodine_mcg=61,
        iron_mg=1.2,
        magnesium_mg=10,
        phosphorus_mg=172,
        potassium_mg=126,
        selenium_mcg=30.8,
        sodium_mg=124,
        zinc_mg=1.1,
    ) * n


def milk_skim_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/171269
    return Nutrient(
        protein=3.6,
        carbs=5.1,
        vitamin_b1_mg=0.05,
        vitamin_b2_mg=0.18,
        vitamin_b3_mg=0.09,
        vitamin_b5_mg=0.36,
        vitamin_b6_mg=0.04,
        vitamin_b9_mcg=5,
        vitamin_b12_mcg=0.5,
        choline_mg=15.6,
        calcium_mg=124,
        iodine_mcg=34,
        magnesium_mg=11,
        phosphorus_mg=101,
        potassium_mg=156,
        selenium_mcg=3.1,
        sodium_mg=50,
        zinc_mg=0.42,
    ) * n


def blueberries_frozen_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/173950
    return Nutrient(
        protein=0.42,
        carbs=12.2,
        fiber=2.7,
        vitamin_c_mg=2.5,
        vitamin_e_mg=0.48,
        vitamin_k_mcg=16.4,
        vitamin_b1_mg=0.03,
        vitamin_b2_mg=0.04,
        vitamin_b3_mg=0.52,
        vitamin_b5_mg=0.13,
        vitamin_b6_mg=0.06,
        vitamin_b9_mcg=7,
        choline_mg=5.1,
        calcium_mg=8,
        iron_mg=0.18,
        magnesium_mg=5,
        phosphorus_mg=11,
        potassium_mg=54,
        zinc_mg=0.07,
    ) * n


def bananas_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/173944
    return Nutrient(
        protein=1.1,
        carbs=22.8,
        fiber=2.6,
        vitamin_c_mg=8.7,
        vitamin_b1_mg=0.03,
        vitamin_b2_mg=0.07,
        vitamin_b3_mg=0.67,
        vitamin_b5_mg=0.33,
        vitamin_b6_mg=0.37,
        vitamin_b9_mcg=20,
        choline_mg=9.8,
        iron_mg=0.26,
        magnesium_mg=27,
        phosphorus_mg=22,
        potassium_mg=358,
        selenium_mcg=1,
        zinc_mg=0.15,
    ) * n


def kiwifruit_zespri_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/168211
    return Nutrient(
        protein=1.02,
        carbs=15.8,
        fiber=1.4,
        vitamin_c_mg=161.3,
        vitamin_e_mg=1.4,
        vitamin_k_mcg=6.1,
        vitamin_b2_mg=0.0,
        vitamin_b3_mg=0.231,
        vitamin_b5_mg=0.12,
        vitamin_b6_mg=0.08,
        vitamin_b9_mcg=31,
        vitamin_b12_mcg=0.08,
        calcium_mg=17,
        magnesium_mg=12,
        phosphorus_mg=25,
        potassium_mg=315,
    ) * n


def carrots_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/170393
    return Nutrient(
        protein=0.93,
        carbs=9.6,
        fiber=2.8,
        vitamin_a_mcg=835,
        vitamin_c_mg=5.9,
        vitamin_e_mg=0.66,
        vitamin_k_mcg=13.2,
        vitamin_b1_mg=0.07,
        vitamin_b2_mg=0.06,
        vitamin_b3_mg=0.98,
        vitamin_b5_mg=0.27,
        vitamin_b6_mg=0.14,
        vitamin_b9_mcg=19,
        choline_mg=8.8,
        calcium_mg=33,
        iron_mg=0.3,
        magnesium_mg=12,
        phosphorus_mg=35,
        potassium_mg=320,
        sodium_mg=69,
        zinc_mg=0.24,
    ) * n


def broccoli_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/170379
    return Nutrient(
        protein=2.8,
        carbs=6.6,
        fiber=2.6,
        vitamin_a_mcg=31,
        vitamin_c_mg=89.2,
        vitamin_e_mg=0.78,
        vitamin_k_mcg=101.6,
        vitamin_b1_mg=0.07,
        vitamin_b2_mg=0.12,
        vitamin_b3_mg=0.64,
        vitamin_b5_mg=0.57,
        vitamin_b6_mg=0.18,
        vitamin_b9_mcg=63,
        choline_mg=18.7,
        calcium_mg=47,
        iron_mg=0.73,
        magnesium_mg=21,
        phosphorus_mg=66,
        potassium_mg=316,
        selenium_mcg=2.5,
        zinc_mg=0.41,
    ) * n


def chicken_breast_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/171077
    return Nutrient(
        protein=21.2,
        fat=0.9,
        vitamin_a_mcg=9,
        vitamin_e_mg=0.56,
        vitamin_b1_mg=0.09,
        vitamin_b2_mg=0.18,
        vitamin_b3_mg=9.6,
        vitamin_b5_mg=1.5,
        vitamin_b6_mg=0.81,
        vitamin_b7_mcg=4,
        vitamin_b12_mcg=0.21,
        choline_mg=82.1,
        iron_mg=0.37,
        magnesium_mg=28,
        phosphorus_mg=213,
        potassium_mg=334,
        selenium_mcg=22.8,
        sodium_mg=328,
        zinc_mg=0.68,
    ) * n


def salmon_farmed_100g(n: float = 1) -> Nutrient:
    # https://tools.myfooddata.com/nutrition-facts/175167
    return Nutrient(
        protein=17.8,
        fat=16.4,
        vitamin_a_mcg=58,
        vitamin_d_mcg=11,
        vitamin_e_mg=3.6,
        vitamin_b1_mg=0.21,
        vitamin_b2_mg=0.16,
        vitamin_b3_mg=8.7,
        vitamin_b5_mg=1.5,
        vitamin_b6_mg=0.64,
        vitamin_b7_mcg=6,
        vitamin_b9_mcg=26,
        vitamin_b12_mcg=3.2,
        choline_mg=78.5,
        iron_mg=0.34,
        magnesium_mg=27,
        phosphorus_mg=240,
        potassium_mg=363,
        selenium_mcg=24,
        sodium_mg=222,
        zinc_mg=0.36,
    ) * n


def nuts_mixed_100g(n: float = 1) -> Nutrient:
    return Nutrient(
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
        protein=10,
        carbs=67.4,
        fat=2.3,
        fiber=7.3,
        calcium_mg=36,
        iron_mg=1.9,
        magnesium_mg=81,
        phosphorus_mg=207,
        potassium_mg=415,
        zinc_mg=1.72,
    ) * n


def oats_probiotics_100g(n: float = 1) -> Nutrient:
    return Nutrient(
        protein=8,
        carbs=56.8,
        fat=11.5,
        fiber=9,
        magnesium_mg=94,
        phosphorus_mg=186,
        potassium_mg=468,
        sodium_mg=25,
    ) * n


def seaweed_snack(n: float = 1) -> Nutrient:
    return Nutrient(
        protein=22.8,
        fat=43.1,
        fiber=19.1,
        vitamin_e_mg=22.9,
        iodine_mcg=2000,
        iron_mg=4.6,
        magnesium_mg=242,
        potassium_mg=1540,
        selenium_mcg=6.8,
        sodium_mg=679,
        zinc_mg=2.58,
    ) * n


def common_meal(n: float = 1) -> Nutrient:
    return Nutrient(
        protein=30,
        carbs=90,
        fat=25,
        fiber=4,
        vitamin_b9_mcg=50,
        calcium_mg=100,
        iron_mg=2,
        magnesium_mg=100,
        potassium_mg=500,
        sodium_mg=1000,
        zinc_mg=3,
    ) * n


if __name__ == '__main__':
    breakfast = oats_probiotics_100g(0.4) + eggs_hard_boiled_100g(1) + blueberries_frozen_100g(0.9) + supplements(1)

    regular_lunch = rice_mixed_100g(0.9) + salmon_farmed_100g(2) + carrots_100g(2) + Nutrient(sodium_mg=1600) * 0.2
    regular_dinner = rice_mixed_100g(0.9) + chicken_breast_100g(0.9) + broccoli_100g(1.5)
    regular_other = milk_skim_100g(2) + kiwifruit_zespri_100g(1)
    regular_day = breakfast + regular_lunch + regular_dinner + regular_other

    workout_lunch = common_meal(1)
    workout_dinner = rice_mixed_100g(0.9) + chicken_breast_100g(0.9) + seaweed_snack(0.05)
    workout_other = milk_skim_100g(2) + nuts_mixed_100g(0.25) + bananas_100g(2) + protein_powder_100g(0.3)
    workout_day = breakfast + workout_lunch + workout_dinner + workout_other

    # print_summary(regular_day, daily_recommended())
    # print_summary(workout_day, daily_recommended())
    # print_summary(regular_day * (2 / 5) + workout_day * (3 / 5), daily_recommended(), show_untracked=True)
    print_summary(regular_day * (2 / 5) + workout_day * (3 / 5), daily_recommended(), show_untracked=False)
