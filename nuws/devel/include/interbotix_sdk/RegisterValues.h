// Generated by gencpp from file interbotix_sdk/RegisterValues.msg
// DO NOT EDIT!


#ifndef INTERBOTIX_SDK_MESSAGE_REGISTERVALUES_H
#define INTERBOTIX_SDK_MESSAGE_REGISTERVALUES_H

#include <ros/service_traits.h>


#include <interbotix_sdk/RegisterValuesRequest.h>
#include <interbotix_sdk/RegisterValuesResponse.h>


namespace interbotix_sdk
{

struct RegisterValues
{

typedef RegisterValuesRequest Request;
typedef RegisterValuesResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct RegisterValues
} // namespace interbotix_sdk


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::interbotix_sdk::RegisterValues > {
  static const char* value()
  {
    return "c4b094ee6f4751519e444f39591c55e1";
  }

  static const char* value(const ::interbotix_sdk::RegisterValues&) { return value(); }
};

template<>
struct DataType< ::interbotix_sdk::RegisterValues > {
  static const char* value()
  {
    return "interbotix_sdk/RegisterValues";
  }

  static const char* value(const ::interbotix_sdk::RegisterValues&) { return value(); }
};


// service_traits::MD5Sum< ::interbotix_sdk::RegisterValuesRequest> should match
// service_traits::MD5Sum< ::interbotix_sdk::RegisterValues >
template<>
struct MD5Sum< ::interbotix_sdk::RegisterValuesRequest>
{
  static const char* value()
  {
    return MD5Sum< ::interbotix_sdk::RegisterValues >::value();
  }
  static const char* value(const ::interbotix_sdk::RegisterValuesRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::interbotix_sdk::RegisterValuesRequest> should match
// service_traits::DataType< ::interbotix_sdk::RegisterValues >
template<>
struct DataType< ::interbotix_sdk::RegisterValuesRequest>
{
  static const char* value()
  {
    return DataType< ::interbotix_sdk::RegisterValues >::value();
  }
  static const char* value(const ::interbotix_sdk::RegisterValuesRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::interbotix_sdk::RegisterValuesResponse> should match
// service_traits::MD5Sum< ::interbotix_sdk::RegisterValues >
template<>
struct MD5Sum< ::interbotix_sdk::RegisterValuesResponse>
{
  static const char* value()
  {
    return MD5Sum< ::interbotix_sdk::RegisterValues >::value();
  }
  static const char* value(const ::interbotix_sdk::RegisterValuesResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::interbotix_sdk::RegisterValuesResponse> should match
// service_traits::DataType< ::interbotix_sdk::RegisterValues >
template<>
struct DataType< ::interbotix_sdk::RegisterValuesResponse>
{
  static const char* value()
  {
    return DataType< ::interbotix_sdk::RegisterValues >::value();
  }
  static const char* value(const ::interbotix_sdk::RegisterValuesResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // INTERBOTIX_SDK_MESSAGE_REGISTERVALUES_H
