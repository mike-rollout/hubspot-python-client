# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GdprClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_crm_v_3_objects_contacts_gdpr_delete_purge(
        self,
        *,
        object_id: str,
        id_property: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently delete a contact and all associated content to follow GDPR. Use optional property 'idProperty' set to 'email' to identify contact by email address. If email address is not found, the email address will be added to a blocklist and prevent it from being used in the future.

        Parameters
        ----------
        object_id : str

        id_property : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from rollout.client import RolloutApi

        client = RolloutApi(
            private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
            private_app="YOUR_PRIVATE_APP",
            token="YOUR_TOKEN",
        )
        client.gdpr.post_crm_v_3_objects_contacts_gdpr_delete_purge(
            object_id="objectId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v3/objects/contacts/gdpr-delete",
            method="POST",
            json={"idProperty": id_property, "objectId": object_id},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGdprClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_crm_v_3_objects_contacts_gdpr_delete_purge(
        self,
        *,
        object_id: str,
        id_property: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently delete a contact and all associated content to follow GDPR. Use optional property 'idProperty' set to 'email' to identify contact by email address. If email address is not found, the email address will be added to a blocklist and prevent it from being used in the future.

        Parameters
        ----------
        object_id : str

        id_property : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from rollout.client import AsyncRolloutApi

        client = AsyncRolloutApi(
            private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
            private_app="YOUR_PRIVATE_APP",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gdpr.post_crm_v_3_objects_contacts_gdpr_delete_purge(
                object_id="objectId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v3/objects/contacts/gdpr-delete",
            method="POST",
            json={"idProperty": id_property, "objectId": object_id},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
