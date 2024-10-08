<div class="grid gap-10 md:gap-8">
  <div
    class="w-full h-full bg-unidLigthPink rounded-lg text-unidDarkBlue border-2 border-unidDarkBlue justify-between xl:flex items-center p-6 space-y-2"
  >
    <!-- prettier-ignore -->
    % if "user_role_id" in user:
    <!-- prettier-ignore -->
    % if user["user_role_id"] == 1:
    <p class="text-unidDarkBlue font-bold text-lg">
      Velkommen, {{ first_name }} {{ last_name }}!
    </p>
    <!-- prettier-ignore -->

    <!-- prettier-ignore -->
    % if current_user.get('has_active_clipcard') and current_user.get('has_active_subscription'):
    <div class="flex gap-1 text-sm">
      <p>Du har et aktivt</p>
      <p class="font-bold">klippekort</p>
      <p>og et</p>
      <p class="font-bold">abonnement</p>
    </div>
    <!-- prettier-ignore -->
    % elif current_user.get('has_active_clipcard'):
    <div class="flex gap-1 text-sm">
      <p>Du har et aktivt</p>
      <p class="font-bold">klippekort</p>
    </div>
    <!-- prettier-ignore -->
    % elif current_user.get('has_active_subscription'):
    <div class="flex gap-1 text-sm">
      <p>Du har et aktivt</p>
      <p class="font-bold">abonnement</p>
    </div>
    <!-- prettier-ignore -->
    % else:
    <div class="flex gap-1 text-sm">
      <p>Du har ikke noget klippekort eller abonnement endnu</p>
    </div>
    <!-- prettier-ignore -->
    % end

    <!-- prettier-ignore -->
    % elif user["user_role_id"] == 2:
    <p class="text-unidDarkBlue font-bold text-lg">
      Velkommen, {{ first_name }} {{ last_name }}!
    </p>
    <div class="flex gap-1 text-sm">
      <p>Du er logget ind som</p>
      <p class="font-bold">admin</p>
    </div>
    % end
    <!-- prettier-ignore -->
    % end
  </div>

  <!-- prettier-ignore -->
  % if user["user_role_id"] == 1: 
    % if current_user and not current_user.get('has_active_clipcard') and "user_role_id" in user:
  <div class="space-y-8">
    <div>
      <div id="content_box_styling">
        <div id="content_box_header_styling">
          <p class="font-bold text-lg text-unidDarkBlue">Klippekort</p>
        </div>
        <div class="flex flex-col gap-10 p-6 text-unidDarkBlue">
          <div
            class="justify-center space-y-1 items-center py-8 lg:py-10 text-center"
          >
            <p class="text-sm font-bold">
              Hov, du har ikke et klippekort endnu...
            </p>
            <p class="text-sm">
              Her vil du kunne få et overblik over timerne på dit klippekort.
            </p>
            <p class="text-sm">
              Klik på 'Klippekort' i menuen, og vælg det klippekort, der passer
              til dig!
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  % else:
  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % include('components/profile/profile_box', box_icon=global_content['ui_icons']['hourglass'], box_title='Tid tilbage', box_content_big=remaining_hours, box_content_medium='timer', box_content_small=remaining_minutes, box_content_xsmall='minutter')
      % include('components/profile/profile_box', box_icon=global_content['ui_icons']['stop_watch'], box_title='Tid brugt', box_content_big=time_used_hours, box_content_medium='timer', box_content_small=time_used_minutes, box_content_xsmall='minutter')
  </div>
  <!-- prettier-ignore -->
  % end
  % end

  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % if "user_role_id" in user: 
      % if  user["user_role_id"] == 2: 
        % include('components/profile/profile_box', box_icon=global_content['ui_icons']['folder_open'], box_title='Åbne klippekort', box_content_big=active_clipcards_count, box_content_medium='klippekort', box_content_small='', box_content_xsmall='')
        % include('components/profile/profile_box', box_icon=global_content['ui_icons']['folder_closed'], box_title='Lukkede klippekort', box_content_big=inactive_clipcards_count, box_content_medium='klippekort', box_content_small='', box_content_xsmall='') 
      % end 
    % end
  </div>
</div>
