#include <nan.h>
#include <QDebug>

void Method(const Nan::FunctionCallbackInfo<v8::Value>& info) {
    qDebug() << "method called";
    info.GetReturnValue().Set(Nan::New("world").ToLocalChecked());
}

void Init(v8::Local<v8::Object> exports) {
    exports->Set(Nan::New("hello").ToLocalChecked(),
                 Nan::New<v8::FunctionTemplate>(Method)->GetFunction());
}

NODE_MODULE(hello, Init)
