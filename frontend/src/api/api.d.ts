import type {
  OpenAPIClient,
  Parameters,
  UnknownParamsObject,
  OperationResponse,
  AxiosRequestConfig,
} from 'openapi-client-axios'; 

declare namespace Components {
    namespace Schemas {
        /**
         * Body_get_token_auth_token_post
         */
        export interface BodyGetTokenAuthTokenPost {
            /**
             * Grant Type
             */
            grant_type?: string; // password
            /**
             * Username
             */
            username: string;
            /**
             * Password
             */
            password: string;
            /**
             * Scope
             */
            scope?: string;
            /**
             * Client Id
             */
            client_id?: string;
            /**
             * Client Secret
             */
            client_secret?: string;
        }
        /**
         * HTTPValidationError
         */
        export interface HTTPValidationError {
            /**
             * Detail
             */
            detail?: /* ValidationError */ ValidationError[];
        }
        /**
         * KeyModel
         */
        export interface KeyModel {
            /**
             * Number
             */
            number: string;
            /**
             * Rentable
             */
            rentable?: boolean;
            /**
             * Checked
             */
            checked?: boolean;
            /**
             * Note
             */
            note?: string;
            /**
             * Id
             */
            id: string; // uuid
            lock: /* LockModelShort */ LockModelShort;
            safe: /* SafeModelShort */ SafeModelShort;
            active_rental?: /* RentalModelShort */ RentalModelShort;
            location: /* LocationModelShort */ LocationModelShort;
            /**
             * Deleted
             */
            deleted: boolean;
        }
        /**
         * KeyModelCreate
         */
        export interface KeyModelCreate {
            /**
             * Number
             */
            number: string;
            /**
             * Rentable
             */
            rentable?: boolean;
            /**
             * Checked
             */
            checked?: boolean;
            /**
             * Note
             */
            note?: string;
            /**
             * Lock Id
             */
            lock_id: string; // uuid
            /**
             * Safe Id
             */
            safe_id: string; // uuid
        }
        /**
         * KeyModelPatch
         */
        export interface KeyModelPatch {
            /**
             * Number
             */
            number?: string;
            /**
             * Rentable
             */
            rentable?: boolean;
            /**
             * Checked
             */
            checked?: boolean;
            /**
             * Note
             */
            note?: string;
            /**
             * Lock Id
             */
            lock_id?: string; // uuid
            /**
             * Safe Id
             */
            safe_id?: string; // uuid
        }
        /**
         * KeyModelShort
         */
        export interface KeyModelShort {
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Number
             */
            number: string;
            lock: /* LockModelShort */ LockModelShort;
            safe: /* SafeModelShort */ SafeModelShort;
        }
        /**
         * LocationModel
         */
        export interface LocationModel {
            /**
             * Name
             */
            name: string;
            /**
             * Address
             */
            address?: string;
            /**
             * Latitude
             */
            latitude?: number;
            /**
             * Longitude
             */
            longitude?: number;
            /**
             * Note
             */
            note?: string;
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Amount Locks
             */
            amount_locks: number;
            /**
             * Amount Safes
             */
            amount_safes: number;
            /**
             * Deleted
             */
            deleted: boolean;
        }
        /**
         * LocationModelCreate
         */
        export interface LocationModelCreate {
            /**
             * Name
             */
            name: string;
            /**
             * Address
             */
            address?: string;
            /**
             * Latitude
             */
            latitude?: number;
            /**
             * Longitude
             */
            longitude?: number;
            /**
             * Note
             */
            note?: string;
        }
        /**
         * LocationModelPatch
         */
        export interface LocationModelPatch {
            /**
             * Name
             */
            name?: string;
            /**
             * Address
             */
            address?: string;
            /**
             * Latitude
             */
            latitude?: number;
            /**
             * Longitude
             */
            longitude?: number;
            /**
             * Note
             */
            note?: string;
        }
        /**
         * LocationModelShort
         */
        export interface LocationModelShort {
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Name
             */
            name: string;
        }
        /**
         * LockModel
         */
        export interface LockModel {
            /**
             * Name
             */
            name: string;
            /**
             * Owner
             */
            owner?: string;
            /**
             * Note
             */
            note?: string;
            location: /* LocationModelShort */ LocationModelShort;
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Amount Keys
             */
            amount_keys: number;
            /**
             * Amount Free Keys
             */
            amount_free_keys: number;
            /**
             * Deleted
             */
            deleted: boolean;
        }
        /**
         * LockModelCreate
         */
        export interface LockModelCreate {
            /**
             * Name
             */
            name: string;
            /**
             * Owner
             */
            owner?: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Location Id
             */
            location_id: string; // uuid
        }
        /**
         * LockModelPatch
         */
        export interface LockModelPatch {
            /**
             * Name
             */
            name?: string;
            /**
             * Owner
             */
            owner?: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Location Id
             */
            location_id?: string; // uuid
        }
        /**
         * LockModelShort
         */
        export interface LockModelShort {
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Name
             */
            name: string;
            location: /* LocationModelShort */ LocationModelShort;
        }
        /**
         * LogEntryModel
         */
        export interface LogEntryModel {
            /**
             * Timestamp
             */
            timestamp: string; // date-time
            /**
             * Message
             */
            message: string;
            creator: /* UserModelShort */ UserModelShort;
            location?: /* LocationModelShort */ LocationModelShort;
            key?: /* KeyModelShort */ KeyModelShort;
            user?: /* UserModelShort */ UserModelShort;
            lock?: /* LockModelShort */ LockModelShort;
            safe?: /* SafeModelShort */ SafeModelShort;
            rental?: /* RentalModelShort */ RentalModelShort;
        }
        /**
         * RentalModel
         */
        export interface RentalModel {
            /**
             * Begin
             */
            begin: string; // date-time
            /**
             * End
             */
            end?: string; // date-time
            /**
             * Allowed By
             * Name of the document that allows the user to rent this key.
             */
            allowed_by?: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Id
             */
            id: string; // uuid
            key: /* KeyModelShort */ KeyModelShort;
            user: /* UserModelShort */ UserModelShort;
            issuing_user: /* UserModelShort */ UserModelShort;
            /**
             * Active
             */
            active: boolean;
            /**
             * Deleted
             */
            deleted: boolean;
        }
        /**
         * RentalModelCreate
         */
        export interface RentalModelCreate {
            /**
             * Begin
             */
            begin?: string; // date-time
            /**
             * End
             */
            end?: string; // date-time
            /**
             * Allowed By
             * Name of the document that allows the user to rent this key.
             */
            allowed_by?: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Key Id
             */
            key_id: string; // uuid
            /**
             * User Id
             */
            user_id: string; // uuid
        }
        /**
         * RentalModelPatch
         */
        export interface RentalModelPatch {
            /**
             * Begin
             */
            begin?: string; // date-time
            /**
             * End
             */
            end?: string; // date-time
            /**
             * Allowed By
             * Name of the document that allows the user to rent this key.
             */
            allowed_by?: string;
            /**
             * Note
             */
            note?: string;
        }
        /**
         * RentalModelShort
         */
        export interface RentalModelShort {
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Begin
             */
            begin: string; // date-time
            /**
             * End
             */
            end?: string; // date-time
            /**
             * User Id
             */
            user_id: string; // uuid
        }
        /**
         * SafeModel
         */
        export interface SafeModel {
            /**
             * Name
             */
            name: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Id
             */
            id: string; // uuid
            location: /* LocationModelShort */ LocationModelShort;
            /**
             * Amount Keys
             */
            amount_keys: number;
            /**
             * Deleted
             */
            deleted: boolean;
        }
        /**
         * SafeModelCreate
         */
        export interface SafeModelCreate {
            /**
             * Name
             */
            name: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Location Id
             */
            location_id: string; // uuid
        }
        /**
         * SafeModelPatch
         */
        export interface SafeModelPatch {
            /**
             * Name
             */
            name?: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Location Id
             */
            location_id?: string; // uuid
        }
        /**
         * SafeModelShort
         */
        export interface SafeModelShort {
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Name
             */
            name: string;
        }
        /**
         * SuccessModel
         */
        export interface SuccessModel {
            /**
             * Success
             */
            success?: boolean;
        }
        /**
         * UserModel
         */
        export interface UserModel {
            /**
             * Login
             */
            login: string;
            /**
             * Name
             */
            name: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Id
             */
            id: string; // uuid
            /**
             * Email
             */
            email: string; // email
            /**
             * Active Rentals
             */
            active_rentals: /* RentalModelShort */ RentalModelShort[];
        }
        /**
         * UserModelShort
         */
        export interface UserModelShort {
            /**
             * Login
             */
            login: string;
            /**
             * Name
             */
            name: string;
            /**
             * Note
             */
            note?: string;
            /**
             * Id
             */
            id: string; // uuid
        }
        /**
         * ValidationError
         */
        export interface ValidationError {
            /**
             * Location
             */
            loc: string[];
            /**
             * Message
             */
            msg: string;
            /**
             * Error Type
             */
            type: string;
        }
    }
}
declare namespace Paths {
    namespace AuthFinish {
        namespace Parameters {
            /**
             * Return Url
             */
            export type ReturnUrl = string;
        }
        export interface QueryParameters {
            return_url: /* Return Url */ Parameters.ReturnUrl;
        }
        namespace Responses {
            export type $200 = any;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace AuthGetToken {
        export type RequestBody = /* Body_get_token_auth_token_post */ Components.Schemas.BodyGetTokenAuthTokenPost;
        namespace Responses {
            export type $200 = any;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace AuthLogin {
        namespace Parameters {
            /**
             * Return Url
             */
            export type ReturnUrl = string;
        }
        export interface QueryParameters {
            return_url: /* Return Url */ Parameters.ReturnUrl;
        }
        namespace Responses {
            export type $200 = any;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace KeyCreateKey {
        export type RequestBody = /* KeyModelCreate */ Components.Schemas.KeyModelCreate;
        namespace Responses {
            export type $200 = /* KeyModel */ Components.Schemas.KeyModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace KeyDeleteKey {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* SuccessModel */ Components.Schemas.SuccessModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace KeyEditKey {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        export type RequestBody = /* KeyModelPatch */ Components.Schemas.KeyModelPatch;
        namespace Responses {
            export type $200 = /* KeyModel */ Components.Schemas.KeyModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace KeyGetKey {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* KeyModel */ Components.Schemas.KeyModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace KeyGetKeys {
        namespace Parameters {
            /**
             * Lock Id
             */
            export type LockId = string; // uuid
            /**
             * Safe Id
             */
            export type SafeId = string; // uuid
        }
        export interface QueryParameters {
            safe_id?: /* Safe Id */ Parameters.SafeId /* uuid */;
            lock_id?: /* Lock Id */ Parameters.LockId /* uuid */;
        }
        namespace Responses {
            /**
             * Response Get Keys Key  Get
             */
            export type $200 = /* KeyModel */ Components.Schemas.KeyModel[];
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LocationCreateLocation {
        export type RequestBody = /* LocationModelCreate */ Components.Schemas.LocationModelCreate;
        namespace Responses {
            export type $200 = /* LocationModel */ Components.Schemas.LocationModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LocationDeleteLocation {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* SuccessModel */ Components.Schemas.SuccessModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LocationEditLocation {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        export type RequestBody = /* LocationModelPatch */ Components.Schemas.LocationModelPatch;
        namespace Responses {
            export type $200 = /* LocationModel */ Components.Schemas.LocationModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LocationGetLocation {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* LocationModel */ Components.Schemas.LocationModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LocationGetLocations {
        namespace Responses {
            /**
             * Response Get Locations Location  Get
             */
            export type $200 = /* LocationModel */ Components.Schemas.LocationModel[];
        }
    }
    namespace LockCreateLock {
        export type RequestBody = /* LockModelCreate */ Components.Schemas.LockModelCreate;
        namespace Responses {
            export type $200 = /* LockModel */ Components.Schemas.LockModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LockDeleteLock {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* SuccessModel */ Components.Schemas.SuccessModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LockEditLock {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        export type RequestBody = /* LockModelPatch */ Components.Schemas.LockModelPatch;
        namespace Responses {
            export type $200 = /* LockModel */ Components.Schemas.LockModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LockGetLock {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* LockModel */ Components.Schemas.LockModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LockGetLocks {
        namespace Parameters {
            /**
             * Location Id
             */
            export type LocationId = string; // uuid
        }
        export interface QueryParameters {
            location_id?: /* Location Id */ Parameters.LocationId /* uuid */;
        }
        namespace Responses {
            /**
             * Response Get Locks Lock  Get
             */
            export type $200 = /* LockModel */ Components.Schemas.LockModel[];
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace LogGetLogs {
        namespace Parameters {
            /**
             * Key Id
             */
            export type KeyId = string; // uuid
            /**
             * Location Id
             */
            export type LocationId = string; // uuid
            /**
             * Lock Id
             */
            export type LockId = string; // uuid
            /**
             * Rental Id
             */
            export type RentalId = string; // uuid
            /**
             * Safe Id
             */
            export type SafeId = string; // uuid
            /**
             * User Id
             */
            export type UserId = string; // uuid
        }
        export interface QueryParameters {
            location_id?: /* Location Id */ Parameters.LocationId /* uuid */;
            key_id?: /* Key Id */ Parameters.KeyId /* uuid */;
            user_id?: /* User Id */ Parameters.UserId /* uuid */;
            lock_id?: /* Lock Id */ Parameters.LockId /* uuid */;
            safe_id?: /* Safe Id */ Parameters.SafeId /* uuid */;
            rental_id?: /* Rental Id */ Parameters.RentalId /* uuid */;
        }
        namespace Responses {
            /**
             * Response Get Logs Log  Get
             */
            export type $200 = /* LogEntryModel */ Components.Schemas.LogEntryModel[];
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace RentalCreateRental {
        export type RequestBody = /* RentalModelCreate */ Components.Schemas.RentalModelCreate;
        namespace Responses {
            export type $200 = /* RentalModel */ Components.Schemas.RentalModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace RentalDeleteRental {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* SuccessModel */ Components.Schemas.SuccessModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace RentalEditRental {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        export type RequestBody = /* RentalModelPatch */ Components.Schemas.RentalModelPatch;
        namespace Responses {
            export type $200 = /* RentalModel */ Components.Schemas.RentalModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace RentalEndRental {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* RentalModel */ Components.Schemas.RentalModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace RentalGetRental {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* RentalModel */ Components.Schemas.RentalModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace RentalGetRentals {
        namespace Parameters {
            /**
             * Issuing User Id
             */
            export type IssuingUserId = string; // uuid
            /**
             * Key Id
             */
            export type KeyId = string; // uuid
            /**
             * User Id
             */
            export type UserId = string; // uuid
        }
        export interface QueryParameters {
            key_id?: /* Key Id */ Parameters.KeyId /* uuid */;
            user_id?: /* User Id */ Parameters.UserId /* uuid */;
            issuing_user_id?: /* Issuing User Id */ Parameters.IssuingUserId /* uuid */;
        }
        namespace Responses {
            /**
             * Response Get Rentals Rental  Get
             */
            export type $200 = /* RentalModel */ Components.Schemas.RentalModel[];
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace SafeCreateSafe {
        export type RequestBody = /* SafeModelCreate */ Components.Schemas.SafeModelCreate;
        namespace Responses {
            export type $200 = /* SafeModel */ Components.Schemas.SafeModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace SafeDeleteSafe {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* SuccessModel */ Components.Schemas.SuccessModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace SafeEditSafe {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        export type RequestBody = /* SafeModelPatch */ Components.Schemas.SafeModelPatch;
        namespace Responses {
            export type $200 = /* SafeModel */ Components.Schemas.SafeModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace SafeGetSafe {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* SafeModel */ Components.Schemas.SafeModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace SafeGetSafes {
        namespace Parameters {
            /**
             * Location Id
             */
            export type LocationId = string; // uuid
        }
        export interface QueryParameters {
            location_id?: /* Location Id */ Parameters.LocationId /* uuid */;
        }
        namespace Responses {
            /**
             * Response Get Safes Safe  Get
             */
            export type $200 = /* SafeModel */ Components.Schemas.SafeModel[];
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace UserGetCurrent {
        namespace Responses {
            export type $200 = /* UserModel */ Components.Schemas.UserModel;
        }
    }
    namespace UserGetUser {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* UserModel */ Components.Schemas.UserModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace UserGetUserProtocol {
        namespace Parameters {
            /**
             * Uuid
             * The UUID of the referenced object.
             */
            export type Uuid = any;
        }
        export interface PathParameters {
            uuid: /**
             * Uuid
             * The UUID of the referenced object.
             */
            Parameters.Uuid;
        }
        namespace Responses {
            export type $200 = /* UserModel */ Components.Schemas.UserModel;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace UserGetUsers {
        namespace Responses {
            /**
             * Response Get Users User  Get
             */
            export type $200 = /* UserModel */ Components.Schemas.UserModel[];
        }
    }
}

export interface OperationMethods {
  /**
   * key_getKeys - Get Keys
   */
  'key_getKeys'(
    parameters?: Parameters<Paths.KeyGetKeys.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.KeyGetKeys.Responses.$200>
  /**
   * key_createKey - Create Key
   */
  'key_createKey'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.KeyCreateKey.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.KeyCreateKey.Responses.$200>
  /**
   * key_getKey - Get Key
   */
  'key_getKey'(
    parameters?: Parameters<Paths.KeyGetKey.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.KeyGetKey.Responses.$200>
  /**
   * key_editKey - Edit Key
   */
  'key_editKey'(
    parameters?: Parameters<Paths.KeyEditKey.PathParameters> | null,
    data?: Paths.KeyEditKey.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.KeyEditKey.Responses.$200>
  /**
   * key_deleteKey - Delete Key
   */
  'key_deleteKey'(
    parameters?: Parameters<Paths.KeyDeleteKey.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.KeyDeleteKey.Responses.$200>
  /**
   * location_getLocations - Get Locations
   */
  'location_getLocations'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LocationGetLocations.Responses.$200>
  /**
   * location_createLocation - Create Location
   */
  'location_createLocation'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.LocationCreateLocation.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LocationCreateLocation.Responses.$200>
  /**
   * location_getLocation - Get Location
   */
  'location_getLocation'(
    parameters?: Parameters<Paths.LocationGetLocation.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LocationGetLocation.Responses.$200>
  /**
   * location_editLocation - Edit Location
   */
  'location_editLocation'(
    parameters?: Parameters<Paths.LocationEditLocation.PathParameters> | null,
    data?: Paths.LocationEditLocation.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LocationEditLocation.Responses.$200>
  /**
   * location_deleteLocation - Delete Location
   */
  'location_deleteLocation'(
    parameters?: Parameters<Paths.LocationDeleteLocation.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LocationDeleteLocation.Responses.$200>
  /**
   * lock_getLocks - Get Locks
   */
  'lock_getLocks'(
    parameters?: Parameters<Paths.LockGetLocks.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LockGetLocks.Responses.$200>
  /**
   * lock_createLock - Create Lock
   */
  'lock_createLock'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.LockCreateLock.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LockCreateLock.Responses.$200>
  /**
   * lock_getLock - Get Lock
   */
  'lock_getLock'(
    parameters?: Parameters<Paths.LockGetLock.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LockGetLock.Responses.$200>
  /**
   * lock_editLock - Edit Lock
   */
  'lock_editLock'(
    parameters?: Parameters<Paths.LockEditLock.PathParameters> | null,
    data?: Paths.LockEditLock.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LockEditLock.Responses.$200>
  /**
   * lock_deleteLock - Delete Lock
   */
  'lock_deleteLock'(
    parameters?: Parameters<Paths.LockDeleteLock.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LockDeleteLock.Responses.$200>
  /**
   * log_getLogs - Get Logs
   */
  'log_getLogs'(
    parameters?: Parameters<Paths.LogGetLogs.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.LogGetLogs.Responses.$200>
  /**
   * rental_getRentals - Get Rentals
   */
  'rental_getRentals'(
    parameters?: Parameters<Paths.RentalGetRentals.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.RentalGetRentals.Responses.$200>
  /**
   * rental_createRental - Create Rental
   */
  'rental_createRental'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.RentalCreateRental.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.RentalCreateRental.Responses.$200>
  /**
   * rental_getRental - Get Rental
   */
  'rental_getRental'(
    parameters?: Parameters<Paths.RentalGetRental.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.RentalGetRental.Responses.$200>
  /**
   * rental_editRental - Edit Rental
   */
  'rental_editRental'(
    parameters?: Parameters<Paths.RentalEditRental.PathParameters> | null,
    data?: Paths.RentalEditRental.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.RentalEditRental.Responses.$200>
  /**
   * rental_deleteRental - Delete Rental
   */
  'rental_deleteRental'(
    parameters?: Parameters<Paths.RentalDeleteRental.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.RentalDeleteRental.Responses.$200>
  /**
   * rental_endRental - End Rental
   */
  'rental_endRental'(
    parameters?: Parameters<Paths.RentalEndRental.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.RentalEndRental.Responses.$200>
  /**
   * safe_getSafes - Get Safes
   */
  'safe_getSafes'(
    parameters?: Parameters<Paths.SafeGetSafes.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.SafeGetSafes.Responses.$200>
  /**
   * safe_createSafe - Create Safe
   */
  'safe_createSafe'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.SafeCreateSafe.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.SafeCreateSafe.Responses.$200>
  /**
   * safe_getSafe - Get Safe
   */
  'safe_getSafe'(
    parameters?: Parameters<Paths.SafeGetSafe.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.SafeGetSafe.Responses.$200>
  /**
   * safe_editSafe - Edit Safe
   */
  'safe_editSafe'(
    parameters?: Parameters<Paths.SafeEditSafe.PathParameters> | null,
    data?: Paths.SafeEditSafe.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.SafeEditSafe.Responses.$200>
  /**
   * safe_deleteSafe - Delete Safe
   */
  'safe_deleteSafe'(
    parameters?: Parameters<Paths.SafeDeleteSafe.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.SafeDeleteSafe.Responses.$200>
  /**
   * user_getUsers - Get Users
   */
  'user_getUsers'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserGetUsers.Responses.$200>
  /**
   * user_getCurrent - Get Current
   */
  'user_getCurrent'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserGetCurrent.Responses.$200>
  /**
   * user_getUser - Get User
   */
  'user_getUser'(
    parameters?: Parameters<Paths.UserGetUser.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserGetUser.Responses.$200>
  /**
   * user_getUserProtocol - Get User Protocol
   */
  'user_getUserProtocol'(
    parameters?: Parameters<Paths.UserGetUserProtocol.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserGetUserProtocol.Responses.$200>
  /**
   * auth_getToken - Get Token
   */
  'auth_getToken'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.AuthGetToken.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.AuthGetToken.Responses.$200>
  /**
   * auth_login - Login
   */
  'auth_login'(
    parameters?: Parameters<Paths.AuthLogin.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.AuthLogin.Responses.$200>
  /**
   * auth_finish - Finish
   */
  'auth_finish'(
    parameters?: Parameters<Paths.AuthFinish.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.AuthFinish.Responses.$200>
}

export interface PathsDictionary {
  ['/key/']: {
    /**
     * key_getKeys - Get Keys
     */
    'get'(
      parameters?: Parameters<Paths.KeyGetKeys.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.KeyGetKeys.Responses.$200>
    /**
     * key_createKey - Create Key
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.KeyCreateKey.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.KeyCreateKey.Responses.$200>
  }
  ['/key/{uuid}']: {
    /**
     * key_getKey - Get Key
     */
    'get'(
      parameters?: Parameters<Paths.KeyGetKey.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.KeyGetKey.Responses.$200>
    /**
     * key_deleteKey - Delete Key
     */
    'delete'(
      parameters?: Parameters<Paths.KeyDeleteKey.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.KeyDeleteKey.Responses.$200>
    /**
     * key_editKey - Edit Key
     */
    'patch'(
      parameters?: Parameters<Paths.KeyEditKey.PathParameters> | null,
      data?: Paths.KeyEditKey.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.KeyEditKey.Responses.$200>
  }
  ['/location/']: {
    /**
     * location_getLocations - Get Locations
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LocationGetLocations.Responses.$200>
    /**
     * location_createLocation - Create Location
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.LocationCreateLocation.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LocationCreateLocation.Responses.$200>
  }
  ['/location/{uuid}']: {
    /**
     * location_getLocation - Get Location
     */
    'get'(
      parameters?: Parameters<Paths.LocationGetLocation.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LocationGetLocation.Responses.$200>
    /**
     * location_deleteLocation - Delete Location
     */
    'delete'(
      parameters?: Parameters<Paths.LocationDeleteLocation.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LocationDeleteLocation.Responses.$200>
    /**
     * location_editLocation - Edit Location
     */
    'patch'(
      parameters?: Parameters<Paths.LocationEditLocation.PathParameters> | null,
      data?: Paths.LocationEditLocation.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LocationEditLocation.Responses.$200>
  }
  ['/lock/']: {
    /**
     * lock_getLocks - Get Locks
     */
    'get'(
      parameters?: Parameters<Paths.LockGetLocks.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LockGetLocks.Responses.$200>
    /**
     * lock_createLock - Create Lock
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.LockCreateLock.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LockCreateLock.Responses.$200>
  }
  ['/lock/{uuid}']: {
    /**
     * lock_getLock - Get Lock
     */
    'get'(
      parameters?: Parameters<Paths.LockGetLock.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LockGetLock.Responses.$200>
    /**
     * lock_deleteLock - Delete Lock
     */
    'delete'(
      parameters?: Parameters<Paths.LockDeleteLock.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LockDeleteLock.Responses.$200>
    /**
     * lock_editLock - Edit Lock
     */
    'patch'(
      parameters?: Parameters<Paths.LockEditLock.PathParameters> | null,
      data?: Paths.LockEditLock.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LockEditLock.Responses.$200>
  }
  ['/log/']: {
    /**
     * log_getLogs - Get Logs
     */
    'get'(
      parameters?: Parameters<Paths.LogGetLogs.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.LogGetLogs.Responses.$200>
  }
  ['/rental/']: {
    /**
     * rental_getRentals - Get Rentals
     */
    'get'(
      parameters?: Parameters<Paths.RentalGetRentals.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.RentalGetRentals.Responses.$200>
    /**
     * rental_createRental - Create Rental
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.RentalCreateRental.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.RentalCreateRental.Responses.$200>
  }
  ['/rental/{uuid}']: {
    /**
     * rental_getRental - Get Rental
     */
    'get'(
      parameters?: Parameters<Paths.RentalGetRental.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.RentalGetRental.Responses.$200>
    /**
     * rental_deleteRental - Delete Rental
     */
    'delete'(
      parameters?: Parameters<Paths.RentalDeleteRental.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.RentalDeleteRental.Responses.$200>
    /**
     * rental_editRental - Edit Rental
     */
    'patch'(
      parameters?: Parameters<Paths.RentalEditRental.PathParameters> | null,
      data?: Paths.RentalEditRental.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.RentalEditRental.Responses.$200>
  }
  ['/rental/{uuid}/end']: {
    /**
     * rental_endRental - End Rental
     */
    'post'(
      parameters?: Parameters<Paths.RentalEndRental.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.RentalEndRental.Responses.$200>
  }
  ['/safe/']: {
    /**
     * safe_getSafes - Get Safes
     */
    'get'(
      parameters?: Parameters<Paths.SafeGetSafes.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.SafeGetSafes.Responses.$200>
    /**
     * safe_createSafe - Create Safe
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.SafeCreateSafe.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.SafeCreateSafe.Responses.$200>
  }
  ['/safe/{uuid}']: {
    /**
     * safe_getSafe - Get Safe
     */
    'get'(
      parameters?: Parameters<Paths.SafeGetSafe.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.SafeGetSafe.Responses.$200>
    /**
     * safe_deleteSafe - Delete Safe
     */
    'delete'(
      parameters?: Parameters<Paths.SafeDeleteSafe.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.SafeDeleteSafe.Responses.$200>
    /**
     * safe_editSafe - Edit Safe
     */
    'patch'(
      parameters?: Parameters<Paths.SafeEditSafe.PathParameters> | null,
      data?: Paths.SafeEditSafe.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.SafeEditSafe.Responses.$200>
  }
  ['/user/']: {
    /**
     * user_getUsers - Get Users
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserGetUsers.Responses.$200>
  }
  ['/user/current']: {
    /**
     * user_getCurrent - Get Current
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserGetCurrent.Responses.$200>
  }
  ['/user/{uuid}']: {
    /**
     * user_getUser - Get User
     */
    'get'(
      parameters?: Parameters<Paths.UserGetUser.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserGetUser.Responses.$200>
  }
  ['/user/{uuid}/pdf']: {
    /**
     * user_getUserProtocol - Get User Protocol
     */
    'get'(
      parameters?: Parameters<Paths.UserGetUserProtocol.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserGetUserProtocol.Responses.$200>
  }
  ['/auth/token']: {
    /**
     * auth_getToken - Get Token
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.AuthGetToken.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.AuthGetToken.Responses.$200>
  }
  ['/auth/start']: {
    /**
     * auth_login - Login
     */
    'get'(
      parameters?: Parameters<Paths.AuthLogin.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.AuthLogin.Responses.$200>
  }
  ['/auth/finish']: {
    /**
     * auth_finish - Finish
     */
    'get'(
      parameters?: Parameters<Paths.AuthFinish.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.AuthFinish.Responses.$200>
  }
}

export type Client = OpenAPIClient<OperationMethods, PathsDictionary>
