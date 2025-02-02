import random

from src.text2image_nsfw import t2i_by_hand
from utils.env import env
from utils.utils import format_str, sleep_for_cool


def prompt():
    positive = "..."
    negative = "..."
    return format_str(positive), format_str(negative)


def t2i():
    positive, negative = prompt()
    resolution = (
        random.choice(["832x1216", "1024x1024", "1216x832"])
        if env.img_size == -1
        else "{}x{}".format(env.img_size[0], env.img_size[1])
    ).split("x")
    scale = env.scale
    sampler = env.sampler
    noise_schedule = env.noise_schedule
    steps = env.steps
    sm = env.sm
    sm_dyn = env.sm_dyn
    seed = random.randint(1000000000, 9999999999) if env.seed == -1 else env.seed
    variety = env.variety
    decrisp = env.decrisp
    img = t2i_by_hand(
        positive,
        negative,
        resolution[0],
        resolution[1],
        scale,
        sampler,
        noise_schedule,
        steps,
        sm,
        sm_dyn,
        seed,
        variety,
        decrisp,
        1,
        True,
        False,
        "",
        "",
        "A1",
    )
    sleep_for_cool(env.t2i_cool_time - 6, env.t2i_cool_time + 6)
    return img[0]
