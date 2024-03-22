# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Product

    id = factory.Sequence(lambda n: n)
   ## Add code to create Fake Products
    name = FuzzyChoice(
        choices=[
            'iPhone',
            'LG OLED-TV',
            'AirPods Max',
            'AirPods Pro',
            'MacBook Pro',
            'MacBook Air',
            'iPad Air',
            'iPad Pro',
            'Nintendo Switch',
            'Apple Watch',
            'Heineken',
            'Flensburger',
            'Absolut Vodka',
            'Havanna Club',
            'GoPro',
            'Tesla Model S',
            'Playstation 5',
            'XBox Series X',
            'North Orbit'
            ]
            )
    description = factory.Faker('text')
    price = FuzzyDecimal(1,2.5,5,100,200,500,1000)
    available = FuzzyChoice(choices=[True,False])
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.SPIRIT,
            Category.BEER,
            Category.KITESURFING,
            Category.AUTOMOTIVE,
            Category.TECH
            ]
            )
