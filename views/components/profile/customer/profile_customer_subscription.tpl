<!-- IF USER DOES NOT HAVE SUBSCRIPTION -->
% if current_user and not current_user.get('has_active_subscription'):
<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_subscription"]["decorative_header_text"] }}
    </p>

    <h2>
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_subscription"]["header_text"] }}
    </h2>
  </div>
  <div class="">
    <!-- prettier-ignore -->
    % for subscription_key, subscription_value in services_and_prices_content['subscription_section']['subscriptions']['subscription_default'].items():
    <div>
      <div
        class="rounded-lg border-2 bg-unidYellow border-unidLightBlue flex flex-col"
      >
        <div class="flex flex-col lg:flex-row justify-between gap-6">
          <div class="text-unidPurple space-y-1 p-6">
            <h3>{{ subscription_value["info"]["hours"] }}</h3>
          </div>
        </div>
        <div class="border-b border-unidLightBlue mx-6"></div>
        <div class="p-6 space-y-6">
          <div class="space-y-2">
            <!-- prettier-ignore -->
            % for point in subscription_value['selling_points']:
            <div class="flex items-center gap-2 text-unidPurple">
              <div class="text-unidPurple w-5 h-5">
                % include(global_content['ui_icons']['checkmark'])
              </div>
              <p>{{ point["text"] }}</p>
            </div>
            % end
          </div>
          <div class="flex items-center justify-between gap-4">
            <p class="text-unidPurple text-base lg:text-lg">Pris</p>
            <div class="flex items-center gap-2">
              <p
                class="text-unidPurple text-right text-2xl xl:text-3xl font-saira font-bold"
              >
                {{ subscription_value["info"]["price"] }}
              </p>
              <div class="flex flex-col text-xs text-unidPurple">
                <p>ekskl.</p>
                <p>moms</p>
              </div>
            </div>
          </div>
          <!-- Display button -->
          <button
            type="button"
            id="primary_button"
            class="buy-button"
            data-subscription-type="{{ subscription_value['info']['hours'] }}"
            data-subscription-price="{{ subscription_value['info']['price'] }}"
            onclick="handleSubscriptionButtonClick(this)"
          >
            {{ subscription_value["button_text"] }}
          </button>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end
  </div>
</div>
<!-- IF USER HAS SUBSCRIPTION -->
% else:
<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_subscription"]["decorative_header_text"] }}
    </p>
    <h2>Dit abonnement</h2>
  </div>
  <div id="content_box_styling">
    <div id="content_box_header_styling">
      <p id="content_box_header_text">Abonnement</p>
    </div>
    <div class="flex flex-col gap-8 p-6 text-unidPurple">
      <!-- USER -->
      <div class="space-y-2 text-sm">
        <div class="space-y-1">
          <p id="form_label">Dit abonnement indeholder:</p>
          <hr />
        </div>
        <div class="space-y-2">
          <div class="flex gap-2">
            <div class="text-unidPurple w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>Kontrol af ydeevne og hastighed for hjemmesiden</p>
          </div>
          <div class="flex gap-2">
            <div class="text-unidPurple w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>Opdatering af tema og plugins</p>
          </div>
          <div class="flex gap-2">
            <div class="text-unidPurple w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>Overvågning af website med Google Search Console</p>
          </div>
          <div class="flex gap-2">
            <div class="text-unidPurple w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>
              30 minutters sparring / vores ekspertise til udbedring af fejl
            </p>
          </div>
        </div>
      </div>
      <!-- prettier-ignore -->
      % if can_cancel:
      <div class="flex w-full justify-end">
        <div class="flex items-center text-red-600">
          <button
            id="cancel-subscription-button"
            type="button"
            class="items-center flex gap-1.5 text-sm font-semibold"
            data-subscription-id="{{ current_user['subscription_id'] }}"
          >
            <div id="icon_small">
              % include(global_content['ui_icons']['trashcan'])
            </div>
            Opsig abonnement
          </button>
        </div>
      </div>
      % else:
      <p class="text-unidPurple text-sm">
        Du kan først opsige dit abonnement efter 1 time.
      </p>
      % end
    </div>
    % end
  </div>
</div>
% end
