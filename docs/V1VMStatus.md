# V1VMStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_name** | **str** | NodeName is the name where the VM is currently running. | [optional]
**migration_node_name** | **str** | MigrationNodeName is the node where the VM is live migrating to. | [optional]
**conditions** | [**list[V1VMCondition]**](V1VMCondition.md) | Conditions are specific points in VM&#39;s pod runtime. | [optional]
**phase** | **str** | Phase is the status of the VM in kubernetes world. It is not the VM status, but partially correlates to it. |
**graphics** | [**list[V1VMGraphics]**](V1VMGraphics.md) | Graphics represent the details of available graphical consoles. |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

