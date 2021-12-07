import 'package:shop_app/domain/state/autorization_state.dart';
import 'package:shop_app/internal/dependencies/repository_module.dart';

class AutorizationModule {
  static AutorizationState autorizationState() {
    return AutorizationState(
      RepositoryTokenModule.userTokenRepository(),
    );
  }
}