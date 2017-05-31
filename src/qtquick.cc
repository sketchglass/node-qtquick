#include <nan.h>
#include <QString>

void Method(const Nan::FunctionCallbackInfo<v8::Value>& info) {
    QString string = "world";
    info.GetReturnValue().Set(Nan::New(string.toUtf8().data()).ToLocalChecked());
}

void Init(v8::Local<v8::Object> exports) {
    exports->Set(Nan::New("hello").ToLocalChecked(),
                 Nan::New<v8::FunctionTemplate>(Method)->GetFunction());
}

NODE_MODULE(hello, Init)
