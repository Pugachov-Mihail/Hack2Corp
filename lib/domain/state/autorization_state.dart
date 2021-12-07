import 'package:mobx/mobx.dart';
import 'package:shop_app/domain/model/user_token.dart';
import 'package:shop_app/domain/repository/user_repository.dart';

part 'autorization_state.g.dart';

class AutorizationState = AutorizationStateBase with _$AutorizationState;

abstract class AutorizationStateBase with Store {
  AutorizationStateBase(this._userTokenRepository);

  final UserTokenRepository? _userTokenRepository;

  @observable
  UserToken? token;

  @observable
  bool isLoading = false;

  @action
  Future<void> getUserToken({
    required String mail,
    required String password,
  }) async {
    isLoading = true;
    final data = await _userTokenRepository!.getUserToken(mail: mail, password: password);
    token = data;
    isLoading = false;
  }
}