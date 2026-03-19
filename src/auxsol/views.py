from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from auxsol.client import AuxsolClient
from core.settings import config
import logging

logger = logging.getLogger(__name__)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_analytics(request):
    """
    Endpoint to get latest analytics data for inverter
    """
    try:
        with AuxsolClient(
            inverter_id=config.AUXSOL_INVERTER_ID,
            inverter_sn=config.AUXSOL_INVERTER_SN
        ) as client:
            res = client.analytics.get_analytics()
            if res and res.get("code") == "AWX-0000":
                data = res.get("data", {})
                energy = data.get("energyData", {})

                return Response({"data": energy}, status=200)
            raise Exception(f"Request Failed: {res}")
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_inverter_report(request):
    """
    Endpoint to get latest analytics report on inverter
    """
    try:
        with AuxsolClient(
            inverter_id=config.AUXSOL_INVERTER_ID,
            inverter_sn=config.AUXSOL_INVERTER_SN
        ) as client:
            res = client.analytics.get_inverter_report()
            if res and res.get("code") == "AWX-0000":
                data = res.get("data", {})

                return Response({"data": data}, status=200)
            raise Exception(f"Request Failed: {res}")
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_inverter(request):
    """
    Endpoint to get latest info on inverter
    """
    try:
        with AuxsolClient(
            inverter_id=config.AUXSOL_INVERTER_ID,
            inverter_sn=config.AUXSOL_INVERTER_SN
        ) as client:
            res = client.inverters.get_inverter()
            if res and res.get("code") == "AWX-0000":
                data = res.get("data", {})

                return Response({"data": data}, status=200)
            raise Exception(f"Request Failed: {res}")
    except Exception as e:
        return Response({"error": str(e)}, status=500)
