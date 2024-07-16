# Reference
## Batch
<details><summary><code>client.batch.<a href="src/rollout/batch/client.py">post_crm_v_3_objects_contacts_batch_read_read</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout import SimplePublicObjectId
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.batch.post_crm_v_3_objects_contacts_batch_read_read(
    properties_with_history=["propertiesWithHistory"],
    inputs=[
        SimplePublicObjectId(
            id="id",
        )
    ],
    properties=["properties"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**properties_with_history:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Sequence[SimplePublicObjectId]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether to return only results that have been archived.
    
</dd>
</dl>

<dl>
<dd>

**id_property:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/rollout/batch/client.py">post_crm_v_3_objects_contacts_batch_archive_archive</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout import SimplePublicObjectId
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.batch.post_crm_v_3_objects_contacts_batch_archive_archive(
    inputs=[
        SimplePublicObjectId(
            id="id",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inputs:** `typing.Sequence[SimplePublicObjectId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/rollout/batch/client.py">post_crm_v_3_objects_contacts_batch_create_create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout import (
    AssociationSpec,
    PublicAssociationsForObject,
    PublicObjectId,
    SimplePublicObjectInputForCreate,
)
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.batch.post_crm_v_3_objects_contacts_batch_create_create(
    inputs=[
        SimplePublicObjectInputForCreate(
            associations=[
                PublicAssociationsForObject(
                    types=[
                        AssociationSpec(
                            association_category="HUBSPOT_DEFINED",
                            association_type_id=1,
                        )
                    ],
                    to=PublicObjectId(
                        id="id",
                    ),
                )
            ],
            properties={
                "email": "bcooper@biglytics.net",
                "phone": "(877) 929-0687",
                "company": "Biglytics",
                "website": "biglytics.net",
                "lastname": "Cooper",
                "firstname": "Bryan",
            },
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inputs:** `typing.Sequence[SimplePublicObjectInputForCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/rollout/batch/client.py">post_crm_v_3_objects_contacts_batch_update_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout import SimplePublicObjectBatchInput
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.batch.post_crm_v_3_objects_contacts_batch_update_update(
    inputs=[
        SimplePublicObjectBatchInput(
            id="1",
            properties={
                "email": "bcooper@biglytics.net",
                "phone": "(877) 929-0687",
                "company": "Biglytics",
                "website": "biglytics.net",
                "lastname": "Cooper",
                "firstname": "Bryan",
            },
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inputs:** `typing.Sequence[SimplePublicObjectBatchInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Basic
<details><summary><code>client.basic.<a href="src/rollout/basic/client.py">get_crm_v_3_objects_contacts_contact_id_get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read an Object identified by `{contactId}`. `{contactId}` refers to the internal object ID. Control what is returned via the `properties` query param.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.basic.get_crm_v_3_objects_contacts_contact_id_get_by_id(
    contact_id="contactId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**properties_with_history:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether to return only results that have been archived.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.basic.<a href="src/rollout/basic/client.py">delete_crm_v_3_objects_contacts_contact_id_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move an Object identified by `{contactId}` to the recycling bin.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.basic.delete_crm_v_3_objects_contacts_contact_id_archive(
    contact_id="contactId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.basic.<a href="src/rollout/basic/client.py">patch_crm_v_3_objects_contacts_contact_id_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a partial update of an Object identified by `{contactId}`. `{contactId}` refers to the internal object ID. Provided property values will be overwritten. Read-only and non-existent properties will be ignored. Properties values can be cleared by passing an empty string.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.basic.patch_crm_v_3_objects_contacts_contact_id_update(
    contact_id="contactId",
    properties={
        "email": "bcooper@biglytics.net",
        "phone": "(877) 929-0687",
        "company": "Biglytics",
        "website": "biglytics.net",
        "lastname": "Cooper",
        "firstname": "Bryan",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.basic.<a href="src/rollout/basic/client.py">get_crm_v_3_objects_contacts_get_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a page of contacts. Control what is returned via the `properties` query param.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.basic.get_crm_v_3_objects_contacts_get_page()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to display per page.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**properties_with_history:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request.
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether to return only results that have been archived.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.basic.<a href="src/rollout/basic/client.py">post_crm_v_3_objects_contacts_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a contact with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard contacts is provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout import AssociationSpec, PublicAssociationsForObject, PublicObjectId
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.basic.post_crm_v_3_objects_contacts_create(
    associations=[
        PublicAssociationsForObject(
            types=[
                AssociationSpec(
                    association_category="HUBSPOT_DEFINED",
                    association_type_id=1,
                )
            ],
            to=PublicObjectId(
                id="id",
            ),
        )
    ],
    properties={
        "email": "bcooper@biglytics.net",
        "phone": "(877) 929-0687",
        "company": "Biglytics",
        "website": "biglytics.net",
        "lastname": "Cooper",
        "firstname": "Bryan",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**associations:** `typing.Sequence[PublicAssociationsForObject]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Public_Object
<details><summary><code>client.public_object.<a href="src/rollout/public_object/client.py">post_crm_v_3_objects_contacts_merge_merge</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.public_object.post_crm_v_3_objects_contacts_merge_merge(
    object_id_to_merge="objectIdToMerge",
    primary_object_id="primaryObjectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id_to_merge:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**primary_object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GDPR
<details><summary><code>client.gdpr.<a href="src/rollout/gdpr/client.py">post_crm_v_3_objects_contacts_gdpr_delete_purge</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a contact and all associated content to follow GDPR. Use optional property 'idProperty' set to 'email' to identify contact by email address. If email address is not found, the email address will be added to a blocklist and prevent it from being used in the future.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.gdpr.post_crm_v_3_objects_contacts_gdpr_delete_purge(
    object_id="objectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id_property:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Search
<details><summary><code>client.search.<a href="src/rollout/search/client.py">post_crm_v_3_objects_contacts_search_do_search</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from rollout import Filter, FilterGroup
from rollout.client import RolloutApi

client = RolloutApi(
    private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
    private_app="YOUR_PRIVATE_APP",
    token="YOUR_TOKEN",
)
client.search.post_crm_v_3_objects_contacts_search_do_search(
    limit=1,
    after="after",
    sorts=["sorts"],
    properties=["properties"],
    filter_groups=[
        FilterGroup(
            filters=[
                Filter(
                    property_name="propertyName",
                    operator="EQ",
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sorts:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_groups:** `typing.Sequence[FilterGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

