# coding: utf-8
from asyncio import get_event_loop
import asyncio
from base64 import b64encode

# This is from PyGithub
from github import Github, InputGitAuthor
from os import environ
from random import choice, randint
from traceback import print_exc
from typing import Dict, List

from chevron.renderer import render
from prettytable import PrettyTable
from requests import get, post
from requests.models import Response


# nclsbayona
async def getDrink(format="string") -> Dict[str, str]:
    """Gets a random drink information from The Cocktail DB API"""
    try:
        the_response: Response = get(
            "https://www.thecocktaildb.com/api/json/v1/1/random.php"
        )
        table_drink: PrettyTable = PrettyTable(["Ingredient", "Measure"])
        response: Dict[str, str] = the_response.json().get("drinks")[0]
        drink: Dict[str, str] = dict()
        drink["drink_name"] = response["strDrink"]
        drink["drink_alcoholic_category"] = response["strAlcoholic"]
        drink["drink_category"] = response["strCategory"]
        drink["drink_instructions"] = response["strInstructions"]
        drink["drink_image"] = response["strDrinkThumb"]
        ingredients: List[str] = list()
        quantities: List[str] = list()
        for key in response:
            if response[key] is not None:
                if key.count("Ingredient") > 0:
                    ingredients.append(response[key])

                elif key.count("Measure") > 0:
                    quantities.append(response[key])

        tot: int = len(quantities)
        for i in range(tot):
            table_drink.add_row([ingredients[i], quantities[i]])

        if format == "string":
            drink["table_drink"] = table_drink.get_string(format=True)
        elif format == "html":
            drink["table_drink"] = table_drink.get_html_string(format=True)
        elif format == "json":
            drink["table_drink"] = table_drink.get_json_string(format=True)
        elif format == "csv":
            drink["table_drink"] = table_drink.get_csv_string(format=True)

        return drink

    except Exception or KeyboardInterrupt:
        return {"error_msj": "An error ocurred please try again"}


async def getAffirmation() -> Dict[str, str]:
    """Gets a translated text from an quote to a random pop character language from funtranslations API"""
    try:
        characters: List[str] = [
            "pirate",
            "minion",
            "sindarin",
            "oldenglish",
            "dothraki",
            "valyrian",
            "vulcan",
            "klingon",
            "yoda",
            "sith",
            "cheunh",
            "gungan",
            "mandalorian",
            "huttese",
        ]
        # Be sure it's a random choice
        translate_to: str = choice(characters)
        #
        choices: int = randint(1, 3)
        response: Response = None
        affirmation: str = None
        if choices == 1:
            response = get("https://affirmations.dev")
            affirmation = (response.json()).get("affirmation")

        elif choices == 2:
            response = get("https://zenquotes.io/api/random")
            affirmation = (response.json())[0].get("q")

        elif choices == 3:
            response = get("https://quotes.rest/qod.json?language=en")
            affirmation = (
                (response.json()).get("contents").get("quotes")[0].get("quote")
            )

        del choices
        text: str = affirmation
        response = get(
            f"https://api.funtranslations.com/translate/{translate_to}.json?text={affirmation}"
        )
        affirmation = (response.json()).get("contents").get("translated")
        affirmation = f'Someone once said: "{affirmation}"'
        text = f'-- "{text}" in {translate_to} language --'

        new_dictionary: Dict[str, str] = dict()
        new_dictionary["text_affirmation1"] = affirmation
        new_dictionary["text_affirmation2"] = text

        """
        if translate_to == "yoda":
            new_dictionary[
                "affirmation_image"
            ] = "https://tukaramatthews.com/wp-content/uploads/2015/03/FullSizeRender.jpg"
        elif translate_to == "pirate":
            new_dictionary[
                "affirmation_image"
            ] = "https://image.flaticon.com/icons/png/512/287/287744.png"
        elif translate_to == "minion":
            new_dictionary[
                "affirmation_image"
            ] = "https://4.bp.blogspot.com/-kLGmroF-doI/VeJhCJlpeyI/AAAAAAAASK4/TRvjlSKu4nk/s1600/13.jpeg"
        elif translate_to == "sindarin":
            new_dictionary[
                "affirmation_image"
            ] = "https://i.etsystatic.com/8273882/r/il/c6deb3/475904358/il_570xN.475904358_enru.jpg"
        elif translate_to == "oldenglish":
            new_dictionary[
                "affirmation_image"
            ] = "https://i.etsystatic.com/21833494/r/il/7e76dd/2140080884/il_570xN.2140080884_ikw0.jpg"
        elif translate_to == "ferblatin":
            new_dictionary[
                "affirmation_image"
            ] = "https://i.ytimg.com/vi/I3nAGsT2skc/maxresdefault.jpg"
        elif translate_to == "dothraki":
            new_dictionary[
                "affirmation_image"
            ] = "https://www.trbimg.com/img-55791e95/turbine/la-oe-0611-peterson-game-of-thrones-dothraki-20150611"
        elif translate_to == "valyrian":
            new_dictionary[
                "affirmation_image"
            ] = "https://duet-cdn.vox-cdn.com/thumbor/0x0:2933x2100/750x500/filters:focal(1716x679:1717x680):format(webp)/cdn0.vox-cdn.com/uploads/chorus_asset/file/3361192/Emilia_Clarke_as_Daenerys_Targaryen__photo_Helen_Sloan_HBO.0.jpg"
        elif translate_to == "vulcan":
            new_dictionary[
                "affirmation_image"
            ] = "https://geneticliteracyproject.org/wp-content/uploads/2017/01/Leonard-Nimoy.png"
        elif translate_to == "klingon":
            new_dictionary[
                "affirmation_image"
            ] = "https://static.independent.co.uk/s3fs-public/thumbnails/image/2016/03/14/19/9-klingon-star-trek.jpg"
        elif translate_to == "pig-latin":
            new_dictionary[
                "affirmation_image"
            ] = "https://miro.medium.com/v2/resize:fit:600/format:png/0*2FCuv0KJMX2knKa0.png"
        elif translate_to == "sith":
            new_dictionary["affirmation_image"] = "https://i.redd.it/ra6s480wfi701.jpg"
        elif translate_to == "cheunh":
            new_dictionary[
                "affirmation_image"
            ] = "https://www.thathashtagshow.com/wp-content/uploads/2019/07/steadfast-1024x655.jpg"
        elif translate_to == "gungan":
            new_dictionary[
                "affirmation_image"
            ] = "https://img1.wikia.nocookie.net/__cb20091012212518/aliens/images/9/93/Gungan-Otolla.jpg"
        elif translate_to == "mandalorian":
            new_dictionary[
                "affirmation_image"
            ] = "https://cdn.dribbble.com/users/2110632/screenshots/5607696/dribbble-03_2x.png"
        elif translate_to == "huttese":
            new_dictionary[
                "affirmation_image"
            ] = "https://static.memrise.com/img/400sqf/from/uploads/course_photos/6265139000150814054627.jpeg"
        """

        return new_dictionary

    except Exception or KeyboardInterrupt:
        return {
            "text_affirmation1": "Always remember ... ",
            "text_affirmation2": "Mistakes don't make you less capable",
        }


async def getWakaStats(waka_key: str = None, format: str = "string") -> Dict[str, str]:
    """Gets WAKATIME API data, and returns in a dictionary some of the information"""
    try:
        dictionary: Dict[str, str] = dict()
        encoded_key: str = str(b64encode(waka_key.encode("utf-8")), "utf-8")
        wakatime_data: Dict = get(
            "https://wakatime.com/api/v1/users/current/stats/last_7_days",
            headers={"Authorization": f"Basic {encoded_key}"},
        ).json()

        # Tables
        table_languages: PrettyTable = PrettyTable(["Language name", "Time spent"])
        temp_list: List[str] = list()
        coded_on: List[Dict[str, str]] = wakatime_data["data"]["languages"]
        for language in coded_on:
            temp_list.clear()
            temp_list.append(language["name"])
            temp_list.append("{hours} hours and {minutes} minutes".format(**language))
            table_languages.add_row(temp_list.copy())

        table_os: PrettyTable = PrettyTable(["OS name", "Time spent"])
        coded_on = wakatime_data["data"]["operating_systems"]

        for os in coded_on:
            temp_list.clear()
            temp_list.append(os["name"])
            temp_list.append("{hours} hours and {minutes} minutes".format(**os))
            table_os.add_row(temp_list.copy())

        if format == "string":
            dictionary["languages"] = table_languages.get_string(format=True)
            dictionary["coded_on_os"] = table_os.get_string(format=True)
        elif format == "html":
            dictionary["languages"] = table_languages.get_html_string(format=True)
            dictionary["coded_on_os"] = table_os.get_html_string(format=True)
        elif format == "json":
            dictionary["languages"] = table_languages.get_json_string(format=True)
            dictionary["coded_on_os"] = table_os.get_json_string(format=True)
        elif format == "csv":
            dictionary["languages"] = table_languages.get_csv_string(format=True)
            dictionary["coded_on_os"] = table_os.get_csv_string(format=True)

        del temp_list, table_os, table_languages
        return dictionary

    except Exception or KeyboardInterrupt:
        return {"error_msj": "An error ocurred please verify your inputs and try again"}


async def getNasaImage(nasa_api_key: str = None) -> Dict[str, str]:
    """Gets the image of the day from NASA Apod API"""
    try:
        the_response: Response = get(
            "https://api.nasa.gov/planetary/apod?api_key=" + nasa_api_key
        )
        response: Dict[str, str] = the_response.json()
        nasa: Dict[str, str] = dict()
        nasa["universe_image_name"] = response["title"]
        nasa[
            "universe_image_copyright"
        ] = f'©️ {response["copyright"]} @ {response["date"]}'.replace("\n", "")
        nasa["universe_image_url"] = response["url"]
        nasa["universe_image_description"] = response["explanation"]

        return nasa

    except Exception or KeyboardInterrupt:
        return {
            "universe_image_name": "Outer Space Background",
            "universe_image_copyright": "Image by rawpixel.com at Freepik",
            "universe_image_url": "https://img.freepik.com/free-photo/outer-space-background_53876-88651.jpg?w=1060&t=st=1695603102~exp=1695603702~hmac=124c2244f1d9fa53cb0a3cb24f182b18e9415ac708fe6b5b501d9eb6ed9b3598",
            "universe_image_description": "Outer Space Background Photo",
        }


async def getAnimals() -> Dict[str, str]:
    """Gets images of animals"""
    try:
        the_response: Response = get("https://api.animality.xyz/img/dog")
        response: Dict[str, str] = the_response.json()
        animals: Dict[str, str] = dict()
        animals["animal_image1"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/duck")
        response: Dict[str, str] = the_response.json()
        animals["animal_image2"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/fox")
        response: Dict[str, str] = the_response.json()
        animals["animal_image3"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/cat")
        response: Dict[str, str] = the_response.json()
        animals["animal_image4"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/bird")
        response: Dict[str, str] = the_response.json()
        animals["animal_image5"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/panda")
        response: Dict[str, str] = the_response.json()
        animals["animal_image6"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/redpanda")
        response: Dict[str, str] = the_response.json()
        animals["animal_image7"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/koala")
        response: Dict[str, str] = the_response.json()
        animals["animal_image8"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/whale")
        response: Dict[str, str] = the_response.json()
        animals["animal_image9"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/dolphin")
        response: Dict[str, str] = the_response.json()
        animals["animal_image10"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/kangaroo")
        response: Dict[str, str] = the_response.json()
        animals["animal_image11"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/bunny")
        response: Dict[str, str] = the_response.json()
        animals["animal_image12"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/lion")
        response: Dict[str, str] = the_response.json()
        animals["animal_image13"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/bear")
        response: Dict[str, str] = the_response.json()
        animals["animal_image14"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/frog")
        response: Dict[str, str] = the_response.json()
        animals["animal_image15"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/penguin")
        response: Dict[str, str] = the_response.json()
        animals["animal_image16"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/axolotl")
        response: Dict[str, str] = the_response.json()
        animals["animal_image17"] = response["link"]
        the_response: Response = get("https://api.animality.xyz/img/capybara")
        response: Dict[str, str] = the_response.json()
        animals["animal_image18"] = response["link"]

        return animals

    except Exception or KeyboardInterrupt:
        return {
            "animal_image1": "https://images.pexels.com/photos/1661179/pexels-photo-1661179.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image2": "https://images.pexels.com/photos/17811/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image3": "https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image4": "https://images.pexels.com/photos/1851164/pexels-photo-1851164.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image5": "https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image6": "https://images.pexels.com/photos/1059823/pexels-photo-1059823.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image7": "https://images.pexels.com/photos/106686/pexels-photo-106686.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image8": "https://images.pexels.com/photos/4666751/pexels-photo-4666751.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image9": "https://images.pexels.com/photos/3396657/pexels-photo-3396657.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image10": "https://images.pexels.com/photos/568022/pexels-photo-568022.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image11": "https://images.pexels.com/photos/674318/pexels-photo-674318.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image12": "https://images.pexels.com/photos/927497/pexels-photo-927497.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image13": "https://images.pexels.com/photos/3493730/pexels-photo-3493730.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image14": "https://images.pexels.com/photos/567540/pexels-photo-567540.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image15": "https://images.pexels.com/photos/41315/africa-african-animal-cat-41315.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image16": "https://images.pexels.com/photos/982230/pexels-photo-982230.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image17": "https://images.pexels.com/photos/4666747/pexels-photo-4666747.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "animal_image18": "https://images.pexels.com/photos/2313396/pexels-photo-2313396.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        }


async def getAll(
    waka_time_api_key: str = None,
    nasa_api_key: str = None,
    format: str = "string",
) -> Dict[str, str]:
    """Gets the information gathered using the rest of the functions"""
    try:
        drink, affirmation, waka, nasa, animals = await asyncio.gather(
            getDrink(format=format),
            getAffirmation(),
            getWakaStats(waka_key=waka_time_api_key, format=format),
            getNasaImage(nasa_api_key=nasa_api_key),
            getAnimals()
        )

    dictionary: Dict[str, str] = {
        **drink,
        **affirmation,
        **waka,
        **nasa,
        **animals
    }

        return dictionary
    except Exception or KeyboardInterrupt as e:
        print(e)
        return {"error_msj": "Error ocurred"}


if __name__ == "__main__":
    try:

        def run_query(query):
            request = post(
                "https://api.github.com/graphql", json={"query": query}, headers=headers
            )
            if request.status_code == 200:
                return request.json()
            else:
                raise Exception(
                    "Query failed to run by returning code of {}. {}".format(
                        request.status_code, query
                    )
                )

        async def updateFile(
            path_to_template_file: str = "/directory_file",
            waka_time_api_key: str = None,
            nasa_api_key: str = None,
            format: str = "string",
        ) -> bool:
            """Updates a file with the information gathered using the rest of the functions"""
            try:
                dictionary = await getAll(
                    waka_time_api_key=waka_time_api_key,
                    nasa_api_key=nasa_api_key,
                    format=format,
                )
                print("The dictionary\n", dictionary)

                with open(path_to_template_file, "r") as template_file:
                    new_readme = render(template_file, dictionary)

                committer = InputGitAuthor(
                    "readme-bot",
                    "41898282+github-actions[bot]@users.noreply.github.com",
                )

                old_readme = repo.get_readme()
                repo.update_file(
                    path=old_readme.path,
                    message="Updated the README file",
                    content=new_readme,
                    sha=old_readme.sha,
                    committer=committer,
                )

                print("\n\nReadme updated\n", new_readme)
                return True
            except Exception or KeyboardInterrupt:
                print_exc()
                return False

        async def main(waka_time_api_key, nasa_api_key, format):
            await updateFile(
                waka_time_api_key=waka_time_api_key,
                nasa_api_key=nasa_api_key,
                format=format,
            )

        waka_api_key = environ["WAKATIME_API_KEY"]
        nasa_api_key = environ["NASA_KEY"]
        ghtoken = environ["GH_TOKEN"]
        format = "html"
        if ghtoken is None:
            raise Exception("Token not available")
        g = Github(ghtoken)
        headers = {"Authorization": "Bearer " + ghtoken}
        # The GraphQL query to get commit data.
        userInfoQuery = """
        {
            viewer {
            login
            email
            id
            }
        }
        """
        user_data = run_query(userInfoQuery)  # Execute the query
        username = user_data["data"]["viewer"]["login"]
        print("Username " + username)
        repo = g.get_repo(f"{username}/{username}")
        loop = get_event_loop()
        loop.run_until_complete(
            main(
                waka_time_api_key=waka_api_key,
                nasa_api_key=nasa_api_key,
                format=format,
            )
        )
        loop.close()
    except Exception as e:
        print("Exception Occurred " + str(e))
        print_exc()
