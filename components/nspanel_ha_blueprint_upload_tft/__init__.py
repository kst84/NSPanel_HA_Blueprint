# __init__.py
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.core import coroutine_with_priority

CODEOWNERS = ["@edwardtfn"]

nspanel_ha_blueprint_upload_tft_ns = cg.esphome_ns.namespace(
    'nspanel_ha_blueprint_upload_tft'
)

CONFIG_SCHEMA = cv.All(
    cv.Schema({}),
)


@coroutine_with_priority(1.0)
async def to_code(config):
    cg.add_define("USE_NSPANEL_HA_BLUEPRINT_UPLOAD_TFT")
    cg.add_global(nspanel_ha_blueprint_upload_tft_ns.using)
