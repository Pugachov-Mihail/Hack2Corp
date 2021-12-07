// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'autorization_state.dart';

// **************************************************************************
// StoreGenerator
// **************************************************************************

// ignore_for_file: non_constant_identifier_names, unnecessary_brace_in_string_interps, unnecessary_lambdas, prefer_expression_function_bodies, lines_longer_than_80_chars, avoid_as, avoid_annotating_with_dynamic

mixin _$AutorizationState on AutorizationStateBase, Store {
  final _$tokenAtom = Atom(name: 'AutorizationStateBase.token');

  @override
  UserToken? get token {
    _$tokenAtom.reportRead();
    return super.token;
  }

  @override
  set token(UserToken? value) {
    _$tokenAtom.reportWrite(value, super.token, () {
      super.token = value;
    });
  }

  final _$isLoadingAtom = Atom(name: 'AutorizationStateBase.isLoading');

  @override
  bool get isLoading {
    _$isLoadingAtom.reportRead();
    return super.isLoading;
  }

  @override
  set isLoading(bool value) {
    _$isLoadingAtom.reportWrite(value, super.isLoading, () {
      super.isLoading = value;
    });
  }

  final _$getUserTokenAsyncAction =
      AsyncAction('AutorizationStateBase.getUserToken');

  @override
  Future<void> getUserToken({required String mail, required String password}) {
    return _$getUserTokenAsyncAction
        .run(() => super.getUserToken(mail: mail, password: password));
  }

  @override
  String toString() {
    return '''
token: ${token},
isLoading: ${isLoading}
    ''';
  }
}
