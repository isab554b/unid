% include('components/header_bar_component')
<header
  class="text-white text-base bg-unidDarkBlue sticky top-0 z-50 transition-all duration-300 ease-in-out"
>
  <div class="width_big py-8 mx-auto flex items-center justify-between">
    <div class="flex">
      <a href="/">
        <!-- prettier-ignore -->
        <img
          class="w-28"
          src="/assets/logos/{{ global_content['logos']['unid']['primary_logo'] }}"
          alt="{{ global_content['logos']['unid']['logo_alt'] }}"
        />
      </a>
    </div>
    <nav class="hidden lg:flex gap-4 xl:gap-8 items-center justify-center">
      % include('elements/nav_items_element')
    </nav>
    <div class="gap-2 lg:gap-4 flex items-center">
      % if user:
      <div class="flex">
        <!-- My account -->
        <!-- prettier-ignore -->
        % include('utilities/buttons/login_button', link='/profile', button_text='Min Konto')
      </div>
      % else:
      <div class="flex">
        <!-- Log in -->
        <!-- prettier-ignore -->
        % include('utilities/buttons/login_button', link='/login', button_text='Log ind')
      </div>
      % end
      <div class="flex lg:hidden">
        % include('utilities/buttons/burger_menu', link='/')
      </div>
    </div>
  </div>

  <!-- Mobil navigation -->
  <nav
    id="mobile-nav"
    class="flex-col flex items-center hidden bg-unidDarkBlue text-white p-4 space-y-2"
  >
    % include('elements/nav_items_element')
  </nav>
</header>
